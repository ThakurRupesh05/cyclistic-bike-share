import pandas as pd
import os


def read_data():
    """
    Read Raw Data Files and return a DataFrame list.
    """

    dataframes = []
    files = os.listdir("Data/raw/")  # list all the raw files in the directory

    for file in files:
        filepath = f"data/raw/{file}"
        new_name = file.replace("-divvy-tirpdata.csv", "_df")
        new_name = pd.read_csv(filepath)
        dataframes.append(new_name)  # append each dataframe into a list

    return dataframes


def clean_dataframe(df_list, columns):
    """
    Process dataframe and return DataFrame list.
    """
    temp_list = []
    for df in df_list:
        df.drop(columns, axis=1, inplace=True)
        temp_list.append(df)

    return pd.concat(temp_list, ignore_index=True)


# list of columns we are not using in our analysis
columns_drop = ["start_station_id", "end_station_id"]

# function calling
df_list = read_data()
final_df = clean_dataframe(df_list, columns_drop)

# writing our final DataFrame
final_df.to_csv("data/processed/tripdata.csv", index=False)
