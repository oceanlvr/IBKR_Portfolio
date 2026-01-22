import pandas as pd


def to_datetime(x):
    """
    transform '20260116' to a proper datetime object
    """
    if not x or pd.isna(x):
        return pd.NaT
    # standard datetime format
    return pd.to_datetime(x, format="%Y%m%d")


def try_numeric(series):
    try:
        # errors='raise' 是关键，它能触发 except 分支
        return pd.to_numeric(series)
    except (ValueError, TypeError):
        return series
