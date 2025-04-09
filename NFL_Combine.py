import glob
import pandas as pd

# define the path, and grab all csv files
csv_files = glob.glob("/Data/Combine/*.csv")

# create empty list to store data frames
all_df = []

# loop through all dfs and store in list
for file in csv_files:
  df = pd.read_csv(file)
  all_df.append(df)

# merge list into one df
combine_df = pd.concat(all_df, ignore_index = True)

combine_df.shape

combine_df.head(5)

# define the path, and grab all csv files
csv_files = glob.glob("/Data/Draft/*.csv")

# create empty list to store data frames
all_df = []

# loop through all dfs and store in list
for file in csv_files:
  df = pd.read_csv(file)
  all_df.append(df)

# merge list into one df
draft_df = pd.concat(all_df, ignore_index = True)

draft_df.shape

draft_df.head(5)
