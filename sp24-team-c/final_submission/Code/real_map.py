import pandas as pd
import folium

data = pd.read_csv('cleaned_PUBLIC_WORKS_VIOLATIONS.csv')
# data2 = pd.read_csv('cleaned_BUILDING_AND_PROPERTY_VIOLATIONS.csv')
geojson_path = 'BPDA_Neighborhood_Boundaries.geojson'

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
# for idx, row in data2.iterrows():
#     folium.CircleMarker([row['latitude'], row['longitude']],
#                         radius=2,
#                         color='rgba(147, 112, 219, 0.5)',
#                         fill=False,
#                         weight=1,
#                         popup=popup_text,
#                         ).add_to(boston_map)
folium.GeoJson(geojson_path, name='geojson').add_to(boston_map)

# Add layer control to toggle on/off
folium.LayerControl().add_to(boston_map)
boston_map.save('boston_violations_map_boundary.html')
