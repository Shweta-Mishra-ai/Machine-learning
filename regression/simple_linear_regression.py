"""Simple Linear Regression script.

Fits a regression line mapping square footage to house prices.
"""

import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

def run_simple_linear_regression(sf_input: float = None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    excel_path = os.path.join(base_dir, "data", "house_price_SLR.xlsx")
    
    if not os.path.exists(excel_path):
        print(f"Dataset not found: {excel_path}")
        return

    df = pd.read_excel(excel_path)
    
    # Feature & target separation
    X = df.iloc[:, :1]
    y = df.iloc[:, -1]
    
    model = LinearRegression()
    model.fit(X, y)
    
    y_pred = model.predict(X)
    
    print("--- Simple Linear Regression Results ---")
    print("Slope (m):        ", model.coef_[0])
    print("Intercept (b):    ", model.intercept_)
    print("R2 Score Accuracy:", r2_score(y, y_pred))
    
    if sf_input is not None:
        prediction = model.predict([[sf_input]])
        print(f"Prediction for {sf_input} sq. feet: ${round(prediction[0], 2)}")

    # Plot (Non-blocking)
    plt.figure(figsize=(6, 4))
    plt.scatter(df["squarefeet"], df["price"], c="green", label="Actual")
    plt.plot(df["squarefeet"], y_pred, c="red", label="Predicted")
    plt.xlabel("Square Feet")
    plt.ylabel("Price")
    plt.title("Simple Linear Regression")
    plt.legend()
    plt.grid(True)
    plt.show(block=False)
    plt.pause(2)
    plt.close()

if __name__ == "__main__":
    run_simple_linear_regression(300)
