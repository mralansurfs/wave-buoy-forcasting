
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_csv_data(filename,time_column = None):
    """
    Function to read the csv data and return the result as a DataFrame.
    Args:
        :param filename: file to read the data from
        :param time_column: optional name of time column to make index
    Returns:
        DataFrame containing the data

    """
    if time_column is None:
        df_data = pd.read_csv(filename)
    else:
        df_data = pd.read_csv(filename).set_index(time_column)
        df_data.index = pd.to_datetime(df_data.index)
        df_data = df_data.rename(columns={time_column: 'timestamp'})
    return df_data

def get_wave_buoy_BOIWB():
    """
    Function to read the bay of islands wave buoy csv data, wind csv data, joint these two datasets
    and return the result as a DataFrame.
    Args:
        only hardcodes for now
    Returns:
        DataFrame containing the wind + wave buoy data
    """
    df_wave = read_csv_data("wave_03_11_24 08_20_52.csv",time_column='Date (NZST)')
    df_wind = read_csv_data("wind_03_11_24 08_20_28.csv",time_column='Date (NZST)')
    df_wind.drop('Site', axis=1, inplace=True)
    df_wave["Site"] = 'BOIWB'
    df_merged_data = pd.merge(df_wave, df_wind, left_index=True, right_index=True)
    return df_merged_data

def basic_data_investigation_plots(df):
    # doing a plot of the number of times a wave of a certain size has been observed
    f, axes = plt.subplots(1, 4)
    sns.histplot(df['Maximum wave height (metres)'], bins=150, linewidth=.2, ax=axes[0])
    sns.histplot(df['Average wave period (seconds)'], bins=150, linewidth=1.2, ax=axes[1])
    sns.histplot(df['Significant wave height (metres)'], bins=150, linewidth=1.2, ax=axes[2])
    sns.histplot(df['Wind gust (knots)'], bins=150, linewidth=1.2, ax=axes[3])
    plt.show()

df_BOIWB = get_wave_buoy_BOIWB()
print(list(df_BOIWB))
basic_data_investigation_plots(df_BOIWB)
plt.show()