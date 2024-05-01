import pandas as pd
import folium
from folium.plugins import MarkerCluster
import numpy as np
import geopandas as gpd
from shapely.geometry import Point

data_path = 'PROPERTY_ASSESSMENT_COORDINATES_FULLY_MERGED.csv'
data = pd.read_csv(data_path, low_memory=False)
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.Longitude, data.Latitude))


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
    'RL - RL': 'Residential land'
}

np.random.seed(42)  # For reproducibility
colors = {lu: '#' + ''.join(np.random.choice(list('0123456789ABCDEF'), size=6)) for lu in lu_descriptions.keys()}

# Create map object
boston_map = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

geojson_path = 'BPDA_Neighborhood_Boundaries.geojson'  # Change this to the path of your GeoJSON file
neighborhoods = gpd.read_file(geojson_path)
folium.GeoJson(geojson_path, name='Boston Neighborhoods').add_to(boston_map)

neighborhood_clusters = {}


for idx, neighborhood in neighborhoods.iterrows():
    neighborhood_name = neighborhood['name']
    for lu in lu_descriptions.keys():
        cluster_name = f'Properties in {neighborhood_name} - {lu_descriptions[lu]}'
        neighborhood_clusters[(neighborhood_name, lu)] = MarkerCluster(name=cluster_name, show=False)
        neighborhood_clusters[(neighborhood_name, lu)].add_to(boston_map)

for idx, property in gdf.iterrows():
    property_neighborhood = None
    for idx, neighborhood in neighborhoods.iterrows():
        if property.geometry.within(neighborhood.geometry):
            property_neighborhood = neighborhood['name']
            break
    if property_neighborhood and property['LU'] in lu_descriptions:
        cluster_key = (property_neighborhood, property['LU'])
        folium.CircleMarker(
            location=[property['Latitude'], property['Longitude']],
            radius=5,
            color=colors[property['LU']],
            fill=True,
            fill_color=colors[property['LU']],
            fill_opacity=0.7,
            popup=f'{lu_descriptions[property["LU"]]}: {property["full_addr"]}'
        ).add_to(neighborhood_clusters[cluster_key])

# Add layer control to toggle on/off different LU categories
folium.LayerControl(collapsed=False).add_to(boston_map)

# Save map
boston_map.save('boston_properties_map_LU.html')