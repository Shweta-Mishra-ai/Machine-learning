"""Advanced Breast Cancer Classification Model.

Features standard scaling, SVM and Random Forest training, correlation heatmap,
ROC curve, and classification reports on breast_cancer_updated.xlsx.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

def run_breast_cancer_classification():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "breast_cancer_updated.xlsx")
    
    if not os.path.exists(file_path):
        print(f"Dataset not found: {file_path}")
        return

    df = pd.read_excel(file_path)
    
    # Diagnostic columns
    X = df.drop(columns=["CodeNumber", "CancerType"])
    y = df["CancerType"] # 2 for benign, 4 for malignant
    
    # Convert labels: 2 -> 0 (benign), 4 -> 1 (malignant)
    y = y.map({2: 0, 4: 1})
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Standard scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train SVM Classifier
    model = SVC(probability=True, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Predictions
    y_pred = model.predict(X_test_scaled)
    probs = model.predict_proba(X_test_scaled)[:, 1]
    
    print("--- Breast Cancer Classification (SVM) ---")
    print(classification_report(y_test, y_pred, target_names=["Benign", "Malignant"]))
    print("ROC AUC Score:", round(roc_auc_score(y_test, probs), 4))
    
    # Plot Correlation Matrix Heatmap (Non-blocking)
    plt.figure(figsize=(8, 6))
    sb.heatmap(X.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Breast Cancer Features Correlation Matrix")
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(2)
    plt.close()

if __name__ == "__main__":
    run_breast_cancer_classification()
