"""Advanced Melbourne House Price Regression Model.

Implements data cleaning (handles missing data through median imputation, drops
unwanted columns), encodes labels, trains a Random Forest Regressor, and
evaluates with MSE and R2 metric outputs.
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def run_melbourne_house_price():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "melbourne.csv")
    
    if not os.path.exists(file_path):
        print(f"Dataset not found: {file_path}")
        return

    df = pd.read_csv(file_path)
    
    # Drop rows without prices (our target variable)
    df.dropna(subset=["Price"], inplace=True)
    
    # Select columns for regression
    num_features = ["Rooms", "Distance", "Bedroom2", "Bathroom", "Car", "Landsize", "BuildingArea"]
    cat_features = ["Type", "Regionname"]
    
    # Simple Imputation of missing values
    for col in num_features:
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)
        
    for col in cat_features:
        df[col].fillna("Unknown", inplace=True)
        
    X = df[num_features + cat_features]
    y = df["Price"]
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Preprocessor using ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features)
        ],
        remainder="passthrough"
    )
    
    X_train_trans = preprocessor.fit_transform(X_train)
    X_test_trans = preprocessor.transform(X_test)
    
    # Train Random Forest Regressor
    model = RandomForestRegressor(n_estimators=50, random_state=42, n_jobs=-1)
    model.fit(X_train_trans, y_train)
    
    y_pred = model.predict(X_test_trans)
    
    # Evaluate
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("--- Melbourne House Price Advanced Regression ---")
    print("R2 Score (Variance Explained):", round(r2, 4))
    print("Root Mean Squared Error (RMSE):", round(np.sqrt(mse), 2))

if __name__ == "__main__":
    run_melbourne_house_price()
