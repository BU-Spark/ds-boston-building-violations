import pandas as pd
import folium

data = pd.read_csv('../data/cleaned_PUBLIC_WORKS_VIOLATIONS.csv.csv')
data2 = pd.read_csv('../data/cleaned_BUILDING_AND_PROPERTY_VIOLATIONS.csv')

boston_map = folium.Map(location=[42.3601, -71.0589], zoom_start=12)
popup_text = f"Violation Count: 1"

for idx, row in data.iterrows():
    folium.CircleMarker([row['latitude'], row['longitude']],
                        radius=2, 
                        color='rgba(255, 0, 0, 0.5)', 
                        fill=False,
                        weight=1,
                        popup=popup_text,
                        ).add_to(boston_map)
for idx, row in data2.iterrows():
    folium.CircleMarker([row['latitude'], row['longitude']],
                        radius=2,
                        color='rgba(147, 112, 219, 0.5)',
                        fill=False,
                        weight=1,
                        popup=popup_text,
                        ).add_to(boston_map)

boston_map.save('boston_violations_map111.html')
