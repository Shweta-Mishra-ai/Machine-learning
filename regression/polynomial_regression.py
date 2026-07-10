"""Polynomial Regression script.

Fits a polynomial curve to model levels vs salaries.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def run_polynomial_regression(level_input: float = None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "Position_Salaries_poly.csv")
    
    if not os.path.exists(csv_path):
        print(f"Dataset not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)
    X = df.iloc[:, 1:2]
    y = df.iloc[:, -1]
    
    # Fit degree 5 curve
    poly = PolynomialFeatures(degree=5)
    X_poly = poly.fit_transform(X)
    
    model = LinearRegression()
    model.fit(X_poly, y)
    y_pred = model.predict(X_poly)
    
    print("--- Polynomial Regression Results ---")
    print("Model Score Accuracy:", model.score(X_poly, y))
    
    if level_input is not None:
        sv = model.predict(poly.transform([[level_input]]))
        print(f"Predicted salary for Level {level_input}: ${round(sv[0], 2)}")

    # Plot (Non-blocking)
    plt.figure(figsize=(6, 4))
    plt.scatter(df["Level"], df["Salary"], c="green", marker="*", label="Actual")
    plt.plot(df["Level"], y_pred, color="red", label="Polynomial Fit")
    plt.xlabel("Level")
    plt.ylabel("Salary")
    plt.title("Polynomial Regression Fit")
    plt.grid(True)
    plt.legend()
    plt.show(block=False)
    plt.pause(2)
    plt.close()

if __name__ == "__main__":
    run_polynomial_regression(6.5)
