import time
import pandas as pd
import googlemaps

# 读取数据集
df = pd.read_csv('PROPERTY_ASSESSMENT_WITH_COORDINATES_UPDATED.csv', dtype={'ZIP_CODE': str}, low_memory=False)
df['ZIP_CODE'] = df['ZIP_CODE'].str.zfill(5)

address_dict = {} 

gmaps = googlemaps.Client(key='')

processed_count = 50000 

for address in df['full_addr'].unique()[processed_count:]:
    if not address or pd.isna(address):
        continue

    if address not in address_dict:
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            latitude = geocode_result[0]['geometry']['location']['lat']
            longitude = geocode_result[0]['geometry']['location']['lng']
            address_dict[address] = (latitude, longitude)
        time.sleep(0.025) 

        processed_count += 1  
        if processed_count % 1000 == 0:
            print(f'Processed {processed_count} addresses.')

df['Latitude'] = df['full_addr'].map(lambda x: address_dict.get(x, (None, None))[0])
df['Longitude'] = df['full_addr'].map(lambda x: address_dict.get(x, (None, None))[1])

df.to_csv('PROPERTY_ASSESSMENT_WITH_COORDINATES_UPDATED_2.csv', index=False)
