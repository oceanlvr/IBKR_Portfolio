from utils.func import to_datetime

ADVANCED_MAP = {
    "account_id": "account_id",
    "acctAlias": "acctAlias",
    "currency": "currency",
    "levelOfDetail": "levelOfDetail",
    "fromDate": {
        "name": "fromDate",
        "transform": to_datetime,
    },
    "toDate": {
        "name": "toDate",
        "transform": to_datetime,
    },
    "startingCash": "startingCash",
    "depositWithdrawals": "depositWithdrawals",
    "netTradesSales": "netTradesSales",
    "netTradesPurchases": "netTradesPurchases",
    "dividends": "dividends",
    "paymentInLieu": "paymentInLieu",
    "brokerFees": "brokerFees",
    "transactionTax": "transactionTax",
    "withholdingTax": "withholdingTax",
    "withholding871m": "withholding871m",
    "brokerInterest": "brokerInterest",
    "insuredDepositInterest": "insuredDepositInterest",
    "fxTranslationGainLoss": "fxTranslationGainLoss",
    "endingCash": "endingCash",
    "endingSettledCash": "endingSettledCash",
    "other": "other",
}
