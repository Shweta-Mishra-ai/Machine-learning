"""Label Encoding and One-Hot Encoding demonstration.

Converts categorical strings into numerical vectors.
"""

import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

def run_label_encoder_ohe():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "dummy_variable_file.csv")
    
    if not os.path.exists(csv_path):
        print(f"Dataset not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)
    print("--- Original Categorical Town Data ---")
    print(df.head())
    
    # Label encoder approach
    le = LabelEncoder()
    df_le = df.copy()
    df_le["town"] = le.fit_transform(df_le["town"])
    print("\n--- Label Encoded town column ---")
    print(df_le.head())
    
    # One-hot encoder approach
    ct = ColumnTransformer(
        [("town_ohe", OneHotEncoder(), [0])],
        remainder="passthrough"
    )
    res = ct.fit_transform(df)
    print("\n--- One Hot Encoded matrix (town columns mapped to dummy variables) ---")
    print(res[:3])

if __name__ == "__main__":
    run_label_encoder_ohe()
