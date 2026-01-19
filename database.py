from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from dotenv import load_dotenv
import os
from pathlib import Path

print(f"registered tables: {list(Base.metadata.tables.keys())}")

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# echo=True debug mode
engine = create_engine(DATABASE_URL, echo=True)

# create Session factory and bind to engine for debugging
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)
