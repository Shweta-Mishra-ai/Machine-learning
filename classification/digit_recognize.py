"""Digits recognition script using Logistic Regression.

Demonstrates model training, evaluation, and classification reports.
"""

from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sb

def run_digit_recognize():
    dataset = load_digits()
    
    X_train, X_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.2, random_state=False
    )
    
    model = LogisticRegression(max_iter=5000)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    print("--- Digits Classification Report ---")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    run_digit_recognize()
