import pandas as pd

file_up = "part1_0.2.csv"

df = pd.read_csv(file_up)

df_no_duplicates = df.drop_duplicates()

df_no_duplicates.to_csv("{}_no_duplicates.csv".format(file_up), index=False)

