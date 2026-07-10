"""Advanced Diabetes Classification Model on PIMA Dataset.

Handles zeros as missing values, performs standard scaling, trains a Random Forest
classifier, and outputs key prediction metrics.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def run_diabetes_classification():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "diabetes.csv")
    
    if not os.path.exists(file_path):
        print(f"Dataset not found: {file_path}")
        return

    df = pd.read_csv(file_path)
    
    # Handle zeros in physiological columns (replace with median values)
    zero_cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    for col in zero_cols:
        df[col] = df[col].replace(0, np.nan)
        df[col].fillna(df[col].median(), inplace=True)
        
    X = df.drop(columns=["Outcome"])
    y = df["Outcome"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Random Forest Classifier
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train_scaled, y_train)
    
    y_pred = rf_model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    
    print("--- PIMA Indian Diabetes Classification (Random Forest) ---")
    print(f"Overall Accuracy: {round(acc * 100, 2)}%")
    print(classification_report(y_test, y_pred, target_names=["Non-Diabetic", "Diabetic"]))
    
    # Plot feature importances (Non-blocking)
    importances = rf_model.feature_importances_
    features = X.columns
    plt.figure(figsize=(8, 5))
    sb.barplot(x=importances, y=features, hue=features, palette="viridis", legend=False)
    plt.title("Feature Importance in Diabetes Classification")
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(2)
    plt.close()

if __name__ == "__main__":
    run_diabetes_classification()
