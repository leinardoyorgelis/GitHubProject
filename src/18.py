import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """
    Load data from a file.
    
    Args:
        file_path (str): The path to the file containing the data.

    Returns:
        DataFrame: A pandas DataFrame loaded from the file.
    """
    # Read the file and return as a DataFrame
    return pd.read_csv(file_path)

# Example usage
file_path = "path_to_your_file.csv"
data = load_data(file_path)
print(data.head())
