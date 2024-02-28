import numpy as np
from scipy.stats import kde
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
from folium.plugins import HeatMap
import folium

# Read the cleaned data
data = pd.read_csv('../data/cleaned_PUBLIC_WORKS_VIOLATIONS.csv')

# Create a GeoDataFrame with a geometry column
geometry = [Point(xy) for xy in zip(data['longitude'], data['latitude'])]
gdf = gpd.GeoDataFrame(data, geometry=geometry)

coords = gdf[['latitude', 'longitude']].values.tolist()

# Create a map centered around the mean location of the coordinates
map_center = gdf[['latitude', 'longitude']].mean().values[::-1]
boston_map = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

# Add a heat map layer to the map
HeatMap(coords).add_to(boston_map)

# Save or display the map
boston_map.save('heatmap.html')
