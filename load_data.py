import pandas as pd

def load_dataset(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        return None
