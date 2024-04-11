import pandas as pd
import folium
from folium.plugins import MarkerCluster
import numpy as np

data_path = 'PROPERTY_ASSESSMENT_COORDINATES_FULLY_MERGED.csv'  # Change this to the path of your CSV file
data = pd.read_csv(data_path, low_memory=False)

lu_descriptions = {
    'A': 'Residential 7 or more units',
    'E': 'Tax-exempt',
    'AH': 'Agricultural/Horticultural',
    'EA': 'Tax-exempt(121A)',
    'C': 'Commercial',
    'I': 'Industrial',
    'CC': 'Commercial condominium',
    'R1': 'Residential 1‐family',
    'CD': 'Residential condominium unit',
    'R2': 'Residential 2‐family',
    'CL': 'Commercial land',
    'R3': 'Residential 3‐family',
    'CM': 'Condominium main',
    'R4': 'Residential 4 or more family',
    'RC': 'Mixed use',
    'CP': 'Condo parking',
    'RL': 'Residential land'
}

np.random.seed(42)  # For reproducibility
colors = {lu: '#' + ''.join(np.random.choice(list('0123456789ABCDEF'), size=6)) for lu in lu_descriptions.keys()}

# Create map object
boston_map = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

geojson_path = 'BPDA_Neighborhood_Boundaries.geojson'  # Change this to the path of your GeoJSON file
folium.GeoJson(geojson_path, name='Boston Neighborhoods').add_to(boston_map)

# Create a MarkerCluster object for each LU category with the proper description
marker_clusters = {lu: MarkerCluster(name=description).add_to(boston_map) for lu, description in lu_descriptions.items()}

# Add markers to the respective cluster with LU description as the name, with the color
for idx, row in data.iterrows():
    if pd.notnull(row['Latitude']) and pd.notnull(row['Longitude']) and row['LU'] in lu_descriptions:
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=5,
            color=colors[row['LU']],
            fill=True,
            fill_color=colors[row['LU']],
            fill_opacity=0.7,
            popup=f'{lu_descriptions[row["LU"]]}: {row["full_addr"]}'
        ).add_to(marker_clusters[row['LU']], show=False)

# Add layer control to toggle on/off different LU categories
folium.LayerControl().add_to(boston_map)

# Save map
boston_map.save('boston_properties_map_LU.html')