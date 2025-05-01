def advanced_frequency_analysis(df, risk_columns):
    frequencies = df[risk_columns].apply(lambda x: x.value_counts()).loc[True]
    return frequencies.fillna(0)
