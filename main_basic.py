# Import necessary functions from other modules
from load_data import load_dataset  # Function to load the dataset
from analyze_basic import basic_analysis  # Function for basic analysis of the dataset

# Main execution block, ensuring the code runs only when executed directly
if __name__ == '__main__':
    # Load the dataset from the specified file path
    df = load_dataset('/Users/odettesaenz/Downloads/webacy_risk_dataset.csv')
    
    # Check if the dataset was loaded successfully
    if df is not None:
        # Perform basic analysis on the loaded dataset
        basic_analysis(df)