import folium
import pandas as pd

df = pd.read_csv('PROPERTY_ASSESSMENT.csv', dtype=str, low_memory=False)
df['ZIP_CODE'] = df['ZIP_CODE'].str.zfill(5)

df['full_addr'] = df['ST_NUM'].astype(str) + ' ' + df['ST_NAME'] + ', ' + df['CITY'] + ', MA'

nan_count = df['full_addr'].str[:3].eq('nan').sum()
print(f'Number of NaN values in full_addr: {nan_count}')

df.loc[df['full_addr'].str[:3] == 'nan', 'full_addr'] = None

df.to_csv('PROPERTY_ASSESSMENT_addr.csv', index=False)
