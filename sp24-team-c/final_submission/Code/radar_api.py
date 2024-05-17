import pandas as pd
import time

# load the data
df = pd.read_csv('PROPERTY_ASSESSMENT_WITH_COORDINATES_UPDATED.csv')

address_dict = {}

# set the number of addresses processed
processed_count = 50000

# get the unique addresses
unique_addresses = df['full_addr'].unique()

for address in unique_addresses[processed_count:]:
    if not address or pd.isna(address):
        continue

    if address not in address_dict:
        try:
            geocoded_df = f_geocode_address_list([address], "")
            latitude = geocoded_df['latitude'][0]  # 获取纬度
            longitude = geocoded_df['longitude'][0]  # 获取经度

            # store the latitude and longitude in the address dictionary
            address_dict[address] = (latitude, longitude)

            time.sleep(0.12)

        except Exception as e:
            print(f"Error processing address {address}: {e}")

    processed_count += 1
    # save the progress
    if processed_count % 100 == 0 or processed_count == len(unique_addresses):
        print(f'Processed {processed_count} addresses.')

# update the DataFrame with the latitude and longitude
df['Latitude'] = df['full_addr'].apply(lambda x: address_dict.get(x, (None, None))[0])
df['Longitude'] = df['full_addr'].apply(lambda x: address_dict.get(x, (None, None))[1])

# save the updated DataFrame to a new CSV file
df.to_csv('PROPERTY_ASSESSMENT_WITH_COORDINATES_UPDATED_2.csv', index=False)
