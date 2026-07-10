"""Simple Linear Regression comparing viewers of The Flash vs Arrow.

Fixes copy-paste plotting and coefficient bugs of the original script.
"""

import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

def run_flash_vs_arrow_regression(episode_num: int = None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    excel_path = os.path.join(base_dir, "data", "flash_vs_arrow_for_SLR.xlsx")
    
    if not os.path.exists(excel_path):
        print(f"Dataset not found: {excel_path}")
        return

    df = pd.read_excel(excel_path)
    
    # Flash regression
    X_flash = df[["flash_episode"]]
    y_flash = df["flash_us_viewers"]
    model_flash = LinearRegression()
    model_flash.fit(X_flash, y_flash)
    y_pred_flash = model_flash.predict(X_flash)
    
    print("--- Flash Series Viewers Model ---")
    print("Flash Slope:    ", model_flash.coef_[0])
    print("Flash Intercept:", model_flash.intercept_)
    
    # Arrow regression
    X_arrow = df[["arrow_episode"]]
    y_arrow = df["arrow_us_viewers"]
    model_arrow = LinearRegression()
    model_arrow.fit(X_arrow, y_arrow)
    y_pred_arrow = model_arrow.predict(X_arrow)
    
    print("\n--- Arrow Series Viewers Model ---")
    # Corrected printing bug: model_arrow.coef_ instead of model_flash.coef_
    print("Arrow Slope:    ", model_arrow.coef_[0])
    print("Arrow Intercept:", model_arrow.intercept_)
    
    if episode_num is not None:
        pred_flash = model_flash.predict([[episode_num]])[0]
        pred_arrow = model_arrow.predict([[episode_num]])[0]
        print(f"\nPredictions for Episode {episode_num}:")
        print(f"  Flash Viewers: {round(pred_flash, 2)} million")
        print(f"  Arrow Viewers: {round(pred_arrow, 2)} million")
        if pred_flash > pred_arrow:
            print("The Flash is predicted to have more viewers.")
        else:
            print("Arrow is predicted to have more viewers.")

    # Plot Corrected Outputs (Non-blocking)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Flash Plot
    ax1.scatter(df["flash_episode"], df["flash_us_viewers"], c="green", label="Actual Viewers")
    # Corrected plotting bug: plot against features (X_flash) rather than targets
    ax1.plot(df["flash_episode"], y_pred_flash, c="red", label="Regression Line")
    ax1.set_xlabel("Flash Episode")
    ax1.set_ylabel("Viewers (Millions)")
    ax1.set_title("The Flash Viewers")
    ax1.grid(True)
    ax1.legend()
    
    # Arrow Plot (Corrected copy-paste bug that plotted Flash data on Arrow graphs)
    ax2.scatter(df["arrow_episode"], df["arrow_us_viewers"], c="blue", label="Actual Viewers")
    ax2.plot(df["arrow_episode"], y_pred_arrow, c="magenta", label="Regression Line")
    ax2.set_xlabel("Arrow Episode")
    ax2.set_ylabel("Viewers (Millions)")
    ax2.set_title("Arrow Viewers")
    ax2.grid(True)
    ax2.legend()
    
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(2)
    plt.close()

if __name__ == "__main__":
    run_flash_vs_arrow_regression(10)
