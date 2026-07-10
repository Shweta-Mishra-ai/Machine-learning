"""K-Nearest Neighbors (KNN) Classifier implemented from scratch.

Classifies loan defaulters based on age and loan amount.
"""

import os
import numpy as np
import pandas as pd

def distance(x: pd.Series, new_age: float, new_loan: float) -> float:
    """Calculate Euclidean distance."""
    return np.sqrt(((x["Age"] - new_age) ** 2) + ((x["Loan"] - new_loan) ** 2))

def knn_classify(new_age: float, new_loan: float, k: int = 3) -> bool:
    """Predict if a person is a loan defaulter using KNN."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    excel_path = os.path.join(base_dir, "data", "loan_repayment_details.xlsx")
    
    if not os.path.exists(excel_path):
        print(f"Dataset not found: {excel_path}")
        return False

    df = pd.read_excel(excel_path)
    df["Distance"] = df.apply(distance, axis=1, args=(new_age, new_loan))
    df.sort_values(by="Distance", ascending=True, inplace=True)
    
    default_subset = df.iloc[:k]
    # Map 'Y' -> 1 and 'N' -> 0
    mapped_defaults = list(default_subset["Default"].map({"Y": 1, "N": 0}))
    
    ones = mapped_defaults.count(1)
    zeros = mapped_defaults.count(0)
    return ones > zeros

def run_knn_scratch():
    print("--- KNN Defaulter Classifier ---")
    new_age, new_loan, k = 30, 50000, 3
    print(f"Testing client: Age={new_age}, Loan={new_loan}, K={k}")
    
    is_defaulter = knn_classify(new_age, new_loan, k)
    if is_defaulter:
        print("Prediction: Loan Defaulter")
    else:
        print("Prediction: NOT a Loan Defaulter")

if __name__ == "__main__":
    run_knn_scratch()
