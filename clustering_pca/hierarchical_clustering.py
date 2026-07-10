"""Hierarchical Clustering script.

Clusters customers based on annual income and spending score.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

def run_hierarchical_clustering():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "Mall_Customers_HC.csv")
    
    if not os.path.exists(csv_path):
        print(f"Dataset not found: {csv_path}")
        return

    dataset = pd.read_csv(csv_path)
    # Features: Annual Income, Spending Score
    X = dataset.iloc[:, 3:5].values
    
    # Train cluster
    hc = AgglomerativeClustering(n_clusters=5, affinity="euclidean", linkage="ward")
    y_hc = hc.fit_predict(X)
    
    print("--- Hierarchical Clustering Complete ---")
    print("Cluster Labels generated for:", len(y_hc), "customers.")
    
    # Plot (Non-blocking)
    plt.figure(figsize=(8, 6))
    colors = ["red", "blue", "green", "cyan", "magenta"]
    for i in range(5):
        plt.scatter(X[y_hc == i, 0], X[y_hc == i, 1], s=100, c=colors[i], label=f"Cluster {i+1}")
    
    plt.title("Clusters of Customers")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score (1-100)")
    plt.legend()
    plt.grid(True)
    plt.show(block=False)
    plt.pause(2)
    plt.close()

if __name__ == "__main__":
    run_hierarchical_clustering()
