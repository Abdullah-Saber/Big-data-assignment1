import pandas as pd
from sklearn.cluster import KMeans

# Load the processed dataset
df = pd.read_csv("res_dpre.csv")

# Select columns for clustering
features = df[["popularity", "vote_average"]]

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(features)

# Count records per cluster and save to a file
cluster_counts = df["cluster"].value_counts()
cluster_counts.to_csv("k.txt")

print("K-means clustering completed and saved as k.txt")
