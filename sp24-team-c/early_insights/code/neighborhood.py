import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
file_path = '../data/cleaned_PUBLIC_WORKS_VIOLATIONS.csv'
violations_df = pd.read_csv(file_path)

# Convert 'status_dttm' to datetime format
violations_df['status_dttm'] = pd.to_datetime(violations_df['status_dttm'])

# Filter records with 'status_dttm' in 2020 and later
violations_df = violations_df[violations_df['status_dttm'].dt.year >= 2020]

# Extract violation_city
violation_cities = violations_df['violation_city']

# Get unique area counts
area_counts = violation_cities.value_counts()

# # Filter out neighborhoods with a count smaller than 50
# filtered_area_counts = area_counts[area_counts >= 50]

# Sort again to make the merged column at the right position
filtered_area_counts_sorted = area_counts.sort_values(ascending=False)

# Set the colors
colors = plt.cm.tab20(np.linspace(0, 1, len(filtered_area_counts_sorted)))

# Plot bar chart
plt.figure(figsize=(10, 8))
filtered_area_counts_sorted.plot(kind='bar', color=colors)  # Use sorted data for plotting
plt.title('Most Affected Neighborhoods in 2020 and Later')
plt.xlabel('Neighborhood')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
