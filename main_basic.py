from load_data import load_dataset
from analyze_basic import basic_analysis

if __name__ == '__main__':
    df = load_dataset('/Users/odettesaenz/Downloads/webacy_risk_dataset.csv')
    if df is not None:
        basic_analysis(df)