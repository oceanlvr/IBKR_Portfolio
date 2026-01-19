from utils.func import to_datetime

ADVANCED_MAP = {
    "accountId": "accountId",
    "acctAlias": "acctAlias",
    "currency": "currency",
    "name": "name",
    "lastTradedDate": {
        "name": "lastTradedDate",
        "transform": to_datetime,
    },
}
