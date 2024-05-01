import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
from collections import defaultdict

# Load your data
data = pd.read_csv('cleaned_311_Service_Requests_2024.csv')
data['text'] = data['case_title'] + ' ' + data['subject'] + ' ' + data['reason'] + ' ' + data['type']

# Load pre-trained DistilBERT model
model = SentenceTransformer('distilbert-base-nli-mean-tokens')

# Encode the text data
encoded_text = model.encode(data['text'])

# Perform clustering using KMeans
# You might need to experiment with the number of clusters (n_clusters) based on your data
# Initialize variables to store the best silhouette score and the corresponding cluster number
best_score = -1
best_n_clusters = 2  # Start with a minimum of 2 clusters

# Try different numbers of clusters
for n_clusters in range(40, 41):  # You can adjust the range as needed
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(encoded_text)
    labels = kmeans.labels_
    silhouette_avg = silhouette_score(encoded_text, labels)
    print("For n_clusters =", n_clusters, "The average silhouette_score is :", silhouette_avg)

    # Update the best score and cluster number if the current score is higher
    if silhouette_avg > best_score:
        best_score = silhouette_avg
        best_n_clusters = n_clusters

# Print the best number of clusters
print("Best number of clusters:", best_n_clusters)

# Perform clustering using the best number of clusters
kmeans = KMeans(n_clusters=best_n_clusters, random_state=0)
kmeans.fit(encoded_text)

# Assign cluster labels to the data
data['cluster'] = kmeans.labels_

# Find the index of the closest sample to the centroid for each cluster
# cluster_representative_indices = defaultdict(int)

# # Find the closest sample to the centroid for each cluster
# for i in range(best_n_clusters):
#     print(f"Processing cluster {i + 1}/{best_n_clusters}")
#     cluster_indices = np.where(kmeans.labels_ == i)[0]
#     centroid = kmeans.cluster_centers_[i]
#     # Get the encoded text for the current cluster
#     cluster_encoded_text = encoded_text[cluster_indices]
#     # Calculate the Euclidean distance between the centroid and all samples in the cluster
#     distances = np.linalg.norm(cluster_encoded_text - centroid, axis=1)
#     # Find the index of the closest sample to the centroid
#     closest_idx = cluster_indices[np.argmin(distances)]
#     cluster_representative_indices[i] = closest_idx

# # Add a column to the data with the cluster representative text
# data['cluster_representative'] = data['cluster'].apply(lambda x: data['text'][cluster_representative_indices[x]])

cluster_representatives = defaultdict(list)
for i, label in enumerate(kmeans.labels_):
    centroid = kmeans.cluster_centers_[label]
    distances = np.linalg.norm(encoded_text - centroid, axis=1)
    closest_idx = np.argmin(distances)
    cluster_representatives[label].append(data['text'][closest_idx])
    print(f"Processed sample {i + 1}/{len(kmeans.labels_)}")

# Add representative text to data['cluster']
data['cluster_representative'] = data['cluster'].apply(lambda x: cluster_representatives[x][0])

# Save the results to a CSV file
data.to_csv('clustered_results_with_representatives.csv', index=False)
print("All clusters processed. Representatives assigned.")
