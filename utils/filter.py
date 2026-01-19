def filter_process_functional(df):
    print(df.head())
    print(df.dtypes)
    # filter by levelOfDetail == SUMMARY
    df = df[df["levelOfDetail"] == "SUMMARY"].copy()
    return df
