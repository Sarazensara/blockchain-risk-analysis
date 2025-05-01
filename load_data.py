import pandas as pd

def load_dataset(file_path):
    """
    Loads a dataset from a given file path using pandas' read_csv function. 
    If the file cannot be loaded, prints an error message and returns None.

    Args:
        file_path (str): The path to the CSV file to be loaded.

    Returns:
        pandas.DataFrame or None: Returns the loaded DataFrame if successful, 
        or None if there is an error while loading the file.
    """
    try:
        # Attempt to load the dataset using pandas read_csv function
        return pd.read_csv(file_path)
    except Exception as e:
        # If an error occurs during file loading, print the error message
        print(f"Error loading file: {e}")
        return None
