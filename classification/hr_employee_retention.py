"""Advanced HR Employee Turnover / Retention Analysis.

One-hot encodes department and salary rankings, processes correlation, and
predicts employee departure probability using a Random Forest classifier.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def run_hr_employee_retention():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "hr_analytics.xlsx")
    
    if not os.path.exists(file_path):
        print(f"Dataset not found: {file_path}")
        return

    df = pd.read_excel(file_path)
    
    # Encode categorical salary rank: low=0, medium=1, high=2
    salary_map = {"low": 0, "medium": 1, "high": 2}
    df["salary_rank"] = df["salary"].map(salary_map)
    df.drop(columns=["salary"], inplace=True)
    
    # One-hot encode department
    df_encoded = pd.get_dummies(df, columns=["Department"], drop_first=True)
    
    X = df_encoded.drop(columns=["left"])
    y = df_encoded["left"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    
    print("--- HR Analytics Turnover Prediction (Random Forest) ---")
    print(f"Model Accuracy: {round(acc * 100, 2)}%")
    print(classification_report(y_test, y_pred, target_names=["Retained", "Left"]))
    
    # Output top predictors of employee departure
    importances = model.feature_importances_
    features = X.columns
    sorted_idx = np.argsort(importances)[::-1]
    
    print("\nTop 5 Predictors of Turnover:")
    for i in range(5):
        print(f"{i+1}. {features[sorted_idx[i]]}: {round(importances[sorted_idx[i]]*100, 2)}%")

if __name__ == "__main__":
    run_hr_employee_retention()
