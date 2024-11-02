
import pandas as pd

def read_csv_data(fname):
    """
    Function to read the csv data and return the result as a DataFrame.
    Args:
        fname (str): file to read the data from
    Returns:
        DataFrame containing the wave buoy data
    """
    df = pd.read_csv(fname).set_index('origintime')
    df.index = pd.to_datetime(df.index)
    return(df)