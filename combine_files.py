# Combining the TXT files into one dataset

import os

import pandas as pd

folder_path = "Datasets/babynames"

frames = []  # empty list to store DataFrames for each year

# Iterating over files in the folder

for file_name in os.listdir(folder_path):
    if file_name.endswith(".txt"):
        # extract the year from the file name

        year = file_name[
            3:7
        ]  # File name format is yobYYYY.txt, it extracts the year using the index slice
        file_path = os.path.join(folder_path, file_name)
        header = ["Name", "Sex", "Number"]  # The columns

        # read txt into a DataFrame

        df = pd.read_csv(file_path, names=header)

        # Add a new coulm 'Year'

        df["Year"] = year

        # Append DataFrame to the list

        frames.append(df)
data = pd.concat(frames, ignore_index=True)  # Combining all the Dataframes into one
df.to_csv("names_1.csv", index=False)  # Expoert the combined df into a csv file
