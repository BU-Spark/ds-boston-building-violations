import pandas as pd
import matplotlib.pyplot as plt

# load the data
data1 = pd.read_csv('cleaned_PUBLIC_WORKS_VIOLATIONS.csv')
data2 = pd.read_csv('cleaned_BUILDING_AND_PROPERTY_VIOLATIONS.csv')

# concatenate the two dataframes
data = pd.concat([data1, data2])

# count the number of violations for each street
street_counts = data['violation_street'].value_counts()

# get the top 20 streets with the most violations
top_streets = street_counts.head(20)

# plot
plt.figure(figsize=(10, 8))
top_streets.plot(kind='bar')
plt.title('Top 20 Violation Streets')
plt.xlabel('Street Name')
plt.ylabel('Number of Violations')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('top_10_violation_streets.png')
plt.show()


