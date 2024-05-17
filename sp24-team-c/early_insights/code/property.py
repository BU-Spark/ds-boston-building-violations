import pandas as pd

# load data
file_path = '../data/property_assessment.csv'
data = pd.read_csv(file_path)

required_columns = ['PID', 'GIS_ID', 'ST_NUM', 'ST_NAME', 'OWNER', 'CITY']

# delete rows missing data
data_filtered = data.dropna(subset=required_columns)

# get new file
data_filtered.to_csv('data/cleaned_property_assessment.csv', index=False)