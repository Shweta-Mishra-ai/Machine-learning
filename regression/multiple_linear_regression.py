"""Multiple Linear Regression script.

Fits a multivariate regression line using square footage, bedrooms, and age
to predict house prices.
"""

import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def run_multiple_linear_regression(predict_sample: list = None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "homeprices.csv")
    
    if not os.path.exists(csv_path):
        print(f"Dataset not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)
    
    # Fill missing values
    med_v = df["bedrooms"].median()
    df.fillna(value=med_v, inplace=True)
    
    X = df.iloc[:, :3]
    y = df.iloc[:, -1]
    
    model = LinearRegression()
    model.fit(X, y)
    
    y_pred = model.predict(X)
    
    print("--- Multiple Linear Regression Results ---")
    print("Coefficients:", model.coef_)
    print("Intercept:   ", model.intercept_)
    print("R2 Score:    ", r2_score(y, y_pred))
    
    if predict_sample:
        sv = model.predict([predict_sample])
        print(f"Prediction for features {predict_sample}: ${round(sv[0], 2)}")

if __name__ == "__main__":
    run_multiple_linear_regression([4050, 4.0, 6])
