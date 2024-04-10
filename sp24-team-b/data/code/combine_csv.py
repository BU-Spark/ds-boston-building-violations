import pandas as pd
import glob

path = "311_*.csv"
all_files = glob.glob(path)

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.to_csv('311_2019_to_present.csv', index=False)