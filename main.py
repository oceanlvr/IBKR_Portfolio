from config.position import ADVANCED_MAP as position_map
from config.account import ADVANCED_MAP as account_map
from config.cash import ADVANCED_MAP as cash_map
from etl import run_etl

# from utils.filter import filter_process_functional
from utils.parse import parse_advanced_mapping_functional

tables_config = [
    {
        "name": "positions",
        "mapping": position_map,
        "node_tag": "OpenPosition",
        "root_tag": "OpenPositions",
    },
    {
        "name": "accounts",
        "mapping": account_map,
        "node_tag": "AccountInformation",
        "root_tag": "FlexStatement",
    },
    {
        "name": "cash",
        "mapping": cash_map,
        "node_tag": "CashReportCurrency",
        "root_tag": "CashReport",
    },
]

if __name__ == "__main__":
    # run_etl()
    for table in tables_config:
        print(f"Processing table: {table['name']}")

        df = parse_advanced_mapping_functional(
            file_path="output/ibkr_statement.xml",
            node_tag=table["node_tag"],
            root_tag=table["root_tag"],
            field_mapping=table["mapping"],
        )

        # df = filter_process_functional(df)
        # print(df.head())
        # print(df.dtypes)

        df.to_csv(f"output/{table['name']}.csv", index=False)
        print(f"Data exported to output/{table['name']}.csv")

        # import to database
        # step.1 write to sync table

        # step.2 read csv and import to table
