def basic_analysis(df):
    print("Column-wise TRUE/FALSE value counts:")
    print(df.apply(lambda x: x.value_counts()).fillna(0))
