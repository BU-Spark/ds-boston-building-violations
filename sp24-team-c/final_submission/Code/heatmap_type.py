import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('cleaned_PUBLIC_WORKS_VIOLATIONS.csv')

# Prepare the data: Group by street and violation type, then count occurrences
grouped = df.groupby(['violation_street', 'description']).size().reset_index(name='count')

# Create a pivot table for the heatmap correctly
pivot_table = grouped.pivot_table(index='violation_street', columns='description', values='count', fill_value=0)

# Generate the heatmap
plt.figure(figsize=(40, 120))
sns.heatmap(pivot_table, cmap="YlGnBu", linewidths=.5, annot=False)
plt.title('Heatmap of Violation Types per Street')
plt.xlabel('Violation Types')
plt.ylabel('Streets')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()  # Adjust layout to not cut off labels
plt.savefig('heatmap.png')
plt.show()

