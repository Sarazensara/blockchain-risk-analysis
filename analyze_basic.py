def basic_analysis(df):
    """
    Performs basic analysis of the DataFrame by counting the occurrence of 'True' and 'False' 
    values for each column, and prints the results.

    Args:
        df (pandas.DataFrame): The DataFrame containing the dataset to be analyzed.
    
    Returns:
        None: This function directly prints the value counts of each column in the DataFrame.
    """
    
    # Print a header indicating that the analysis of TRUE/FALSE value counts is about to begin
    print("Column-wise TRUE/FALSE value counts:")
    
    # Apply value_counts() across all columns to count occurrences of each unique value (True/False).
    # Use fillna(0) to replace any missing values with 0 (in case some columns have only one value).
    print(df.apply(lambda x: x.value_counts()).fillna(0))
