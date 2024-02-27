#author is Chloe 
import pandas as pd


# Load the data
file_path = '/Users/chloe/Desktop/BUILDING AND PROPERTY VIOLATIONS.csv'
data = pd.read_csv(file_path)

# Normalize the city names to ensure consistent counting
data['normalized_city'] = data['violation_city'].str.lower().str.strip()

# Count the number of violations by normalized city
normalized_violation_counts = data['normalized_city'].value_counts()

# Display the count of violations by normalized city
print(normalized_violation_counts)

