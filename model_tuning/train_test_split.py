"""Model validation split demonstration.

Fits a simple regression on training splits and tests on testing splits.
"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def run_train_test_split():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "canada_per_capita_income_DTR.csv")
    
    if not os.path.exists(csv_path):
        print(f"Dataset not found: {csv_path}")
        return

    df = pd.read_csv(csv_path)
    X = df.iloc[:, :1]
    y = df.iloc[:, -1]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=False
    )
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    print("--- Train Test Split Results ---")
    print("Train dataset length:", len(X_train))
    print("Test dataset length: ", len(X_test))
    print("R2 Score (Train):    ", model.score(X_train, y_train))
    print("R2 Score (Test):     ", r2_score(y_test, y_pred))

if __name__ == "__main__":
    run_train_test_split()
