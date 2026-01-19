from utils.func import to_datetime

ADVANCED_MAP = {
    "conid": "conid",  # primary key
    "symbol": "symbol",
    "isin": "isin",
    # core data start
    "position": "position",
    "markPrice": "markPrice",
    "positionValue": "positionValue",
    "openPrice": "openPrice",
    "costBasisPrice": "costBasisPrice",
    "costBasisMoney": "costBasisMoney",
    "fifoPnlUnrealized": "fifoPnlUnrealized",
    "percentOfNAV": "percentOfNAV",
    "side": "side",
    # core data end
    "reportDate": {
        "name": "reportDate",
        "transform": to_datetime,
    },
    "assetCategory": "assetCategory",
    "subCategory": "subCategory",
    "listingExchange": "listingExchange",
    "currency": "currency",
    "fxRateToBase": "fxRateToBase",
    "levelOfDetail": "levelOfDetail",  # SUMMARY / LOT
}
