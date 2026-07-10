"""Min-Max Scaling script.

Normalizes feature column elements. Protects against zero range divisions.
"""

import os
import numpy as np
import pandas as pd

def min_max_scale(X: np.ndarray) -> np.ndarray:
    """Normalize features using custom min-max calculation."""
    mins = np.min(X, axis=0)
    maxs = np.max(X, axis=0)
    ranges = maxs - mins
    
    # Safety protection for constant columns (range == 0)
    ranges_safe = np.where(ranges == 0, 1e-9, ranges)
    return (X - mins) / ranges_safe

def run_min_max_scaling():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "homeprices.csv")
    
    if not os.path.exists(csv_path):
        print(f"Dataset not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)
    med_v = df["bedrooms"].median()
    df.fillna(value=med_v, inplace=True)
    
    X = df.iloc[:, :3].values
    scaled_X = min_max_scale(X)
    print("--- Min-Max Scaled home price features ---")
    print(scaled_X[:3])

if __name__ == "__main__":
    run_min_max_scaling()
