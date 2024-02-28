# Re-importing the necessary libraries and the dataset
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df1 = pd.read_csv('../data/cleaned_PUBLIC_WORKS_VIOLATIONS.csv')
d2f = pd.read_csv('../data/cleaned_BUILDING_AND_PROPERTY_VIOLATIONS.csv')

# Concatenate the two dataframes
df = pd.concat([df1, d2f])

# Count the occurrences of each 'sam_id'
sam_id_counts = df['sam_id'].value_counts()

# Filter 'sam_id' with more than one occurrence
multiple_violations = sam_id_counts[sam_id_counts > 1].index

# Filter the dataframe to get rows with 'sam_id' that have more than one occurrence
df_multiple_violations = df[df['sam_id'].isin(multiple_violations)]

# Now, group by 'violation_street' and count the occurrences
street_counts = df_multiple_violations.groupby('violation_street').size()

# Filter streets with more than two violations and remove the condition for greater than two counts
streets = street_counts.sort_values(ascending=False).head(20)
print(streets.index)
# Plot the results x is the street name and y is the number of violations
plt.figure(figsize=(12, 6))
streets.plot(kind='bar')
plt.title('Streets with Multiple Violations')
plt.xlabel('Street Name')
plt.ylabel('Number of Violations')
plt.xticks(ticks=np.arange(len(streets)), labels=streets.index, rotation=90, fontsize=6)
plt.tight_layout()  # Adjust layout to not cut off x-labels
# save the plot
plt.savefig('streets_with_multiple_violations.png')
plt.show()



