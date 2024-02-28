import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
property_df = pd.read_csv('../data/cleaned_property_assessment.csv')
violations_df = pd.read_csv('../data/cleaned_BUILDING_AND_PROPERTY_VIOLATIONS.csv')

# Function to concatenate address components with space
def concatenate_address(num, street, suffix=None):
    try:
        num = int(float(num))
    except ValueError:
        pass
    parts = [str(num), str(street)]
    if suffix and str(suffix).strip():
        parts.append(str(suffix))
    address = " ".join(parts).lower().strip()
    return address


# Concatenate address components for the property dataset
property_df['full_address'] = property_df.apply(lambda x: concatenate_address(x['ST_NUM'], x['ST_NAME']), axis=1)
# print(property_df['full_address'])

# Concatenate address components for the building violations dataset
violations_df['full_address'] = violations_df.apply(lambda x: concatenate_address(x['violation_stno'], x['violation_street'], x.get('violation_suffix', '')), axis=1)

# Match addresses between datasets, ensure 'owner' column is included from the property dataset in the merge
matched_addresses = pd.merge(violations_df, property_df[['full_address', 'OWNER']], on='full_address', how='inner')
# Count the number of violations by owner
owner_violation_counts = matched_addresses['OWNER'].value_counts().reset_index()
owner_violation_counts.columns = ['Owner', 'Violation_Count']
print(owner_violation_counts)

top_owners = owner_violation_counts.head(10)  # Taking top 10 owners for a cleaner plot

plt.figure(figsize=(10, 6))
plt.bar(top_owners['Owner'], top_owners['Violation_Count'], color='skyblue')
plt.xlabel('Owner')
plt.ylabel('Number of Violations')
plt.xticks(rotation=45, ha="right")
plt.title('Top 10 Owners by Number of Violations')
plt.tight_layout()  # Adjust layout to not cut off labels
plt.show()