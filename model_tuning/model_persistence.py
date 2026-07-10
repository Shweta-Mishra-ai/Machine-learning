"""Model Serialization (Persistence) using pickle and joblib.

Fits a regression model and saves it. Resolves sklearn.externals deprecations.
"""

import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import joblib

def run_model_persistence():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    excel_path = os.path.join(base_dir, "data", "house_price_SLR.xlsx")
    
    if not os.path.exists(excel_path):
        print(f"Dataset not found: {excel_path}")
        return

    df = pd.read_excel(excel_path)
    X = df.iloc[:, :1]
    y = df.iloc[:, -1]
    
    lr = LinearRegression()
    lr.fit(X, y)
    
    # Local paths for serialized files
    pickle_path = os.path.join(base_dir, "model_tuning", "lr_model.pkl")
    joblib_path = os.path.join(base_dir, "model_tuning", "lr_model.joblib")
    
    # Pickle dump & load
    with open(pickle_path, "wb") as f:
        pickle.dump(lr, f)
    print("--- Model saved via Pickle ---")
    
    with open(pickle_path, "rb") as f:
        pickle_lr = pickle.load(f)
    print("Pickle Predict:", pickle_lr.predict([[320]])[0])
    
    # Joblib dump & load (using root joblib module instead of sklearn.externals)
    joblib.dump(lr, joblib_path)
    print("--- Model saved via Joblib ---")
    
    joblib_lr = joblib.load(joblib_path)
    print("Joblib Predict:", joblib_lr.predict([[320]])[0])
    
    # Cleanup temp models
    if os.path.exists(pickle_path):
        os.remove(pickle_path)
    if os.path.exists(joblib_path):
        os.remove(joblib_path)

if __name__ == "__main__":
    run_model_persistence()
