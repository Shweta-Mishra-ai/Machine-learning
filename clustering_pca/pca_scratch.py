"""Principal Component Analysis (PCA) scratch vs sklearn verification.

Fixes unexpected indentation error from the legacy script.
"""

from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sb

def run_pca():
    dataset = load_iris()
    ORIGINAL_MATRIX = dataset.data
    
    IRIS_COV_MATRIX = np.cov(ORIGINAL_MATRIX, rowvar=False)
    
    pca = PCA(n_components=None)
    pca_matrix = pca.fit_transform(ORIGINAL_MATRIX)
    
    eigen_values, eigen_vectors = np.linalg.eig(IRIS_COV_MATRIX)
    
    FEATURE_MATRIX = eigen_vectors[:, :2]
    FEATURE_MATRIX_T = np.transpose(FEATURE_MATRIX)
    ORIGINAL_MATRIX_T = np.transpose(ORIGINAL_MATRIX)
    
    FINAL_MATRIX = np.matmul(FEATURE_MATRIX_T, ORIGINAL_MATRIX_T)
    FINAL_MATRIX_T = np.transpose(FINAL_MATRIX)
    
    # Corrected formatting / indentation bug of the original PCA.txt code
    data = pd.DataFrame(data=FINAL_MATRIX_T, columns=["PC1", "PC2"])
    y_series = pd.Series(dataset.target)
    y_series = y_series.replace(0, "setosa")
    y_series = y_series.replace(1, "versicolor")
    y_series = y_series.replace(2, "virginica")
    data["target"] = y_series
    
    print("--- PCA Transformed Iris Sample ---")
    print(data.head())
    
    # Seaborn plot (Non-blocking)
    plt.figure(figsize=(6, 4))
    sb.scatterplot(x="PC1", y="PC2", data=data, hue="target")
    plt.title("Iris Projection on First Two PCA components")
    plt.show(block=False)
    plt.pause(2)
    plt.close()

if __name__ == "__main__":
    run_pca()
