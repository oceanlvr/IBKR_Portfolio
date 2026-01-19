import time
import requests
import xml.etree.ElementTree as ET
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

VERSION = "3"

TOKEN = os.getenv("TOKEN")
QUERY_ID = os.getenv("QUERY_ID")
send_url = os.getenv("SEND_URL")
get_url = os.getenv("GET_URL")

engine = create_engine(DB_URL)


def run_etl():
    params = {"t": TOKEN, "q": QUERY_ID, "v": VERSION}

    resp = requests.get(send_url, params=params)
    if resp.status_code != 200:
        print(f"Failed to initiate request: {resp.text}")
        return

    # parse and get `ReferenceCode`
    root = ET.fromstring(resp.content)
    if root.find("Status").text == "Warn":
        print(f"IBKR Warning: {root.find('ErrorMessage').text}")
        return

    ref_code = root.find("ReferenceCode").text
    print(f"Received ReferenceCode: {ref_code}")

    # record to sync log
    with engine.begin() as conn:
        conn.execute(
            text(
                "INSERT INTO ibkr_sync_logs (reference_code, query_id, status) VALUES (:r, :q, 'PENDING')"
            ),
            {"r": ref_code, "q": QUERY_ID},
        )

    get_params = {"t": TOKEN, "q": ref_code, "v": VERSION}

    while True:
        print("Polling for data...")
        data_resp = requests.get(get_url, params=get_params)

        # IBKR Error Code 1019 - Data Not Ready
        if "1019" in data_resp.text:
            time.sleep(20)
            continue

        if data_resp.status_code == 200:
            parse_and_save(data_resp.content, ref_code)
            with engine.begin() as conn:
                conn.execute(
                    text(
                        "UPDATE ibkr_sync_logs SET status='COMPLETED' WHERE reference_code=:r AND query_id=:q"
                    ),
                    {"r": ref_code, "q": QUERY_ID},
                )
            break
        else:
            print(f"Error fetching statement: {data_resp.text}")
            break


def parse_and_save(xml_content, ref_code):
    """parse XML and save to file"""
    with open("output/ibkr_statement.xml", "wb") as f:
        f.write(xml_content)
    print("Statement saved to output/ibkr_statement.xml")


if __name__ == "__main__":
    run_etl()
