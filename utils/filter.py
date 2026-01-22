def filter_process_functional(df):
    # filter by levelOfDetail == SUMMARY
    df = df[df["levelOfDetail"] == "SUMMARY"].copy()
    return df
