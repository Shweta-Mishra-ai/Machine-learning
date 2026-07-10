"""Gaussian Naive Bayes Classifier implemented from scratch.

Features standard deviation safety checks to prevent division-by-zero crashes.
"""

import os
import numpy as np
import pandas as pd
from functools import reduce

def gaussian_naive_bayes(new_data: np.ndarray, mean: pd.Series, std: pd.Series) -> float:
    """Compute Gaussian Naive Bayes probability for sample features."""
    # Prevent divide-by-zero by replacing zeros with a tiny epsilon
    std_safe = np.where(std == 0, 1e-9, std)
    prob = (1 / (np.sqrt(2 * np.pi) * std_safe)) * np.exp(-((new_data - mean) ** 2) / (2 * (std_safe ** 2)))
    return reduce(lambda x, y: x * y, prob)

def run_gaussian_nb_scratch():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    excel_path = os.path.join(base_dir, "data", "Weather_Dataset_for_GNB.xlsx")
    
    if not os.path.exists(excel_path):
        print(f"Dataset not found: {excel_path}")
        return

    df = pd.read_excel(excel_path)
    df_yes = df[df["Play"] == "Yes"]
    df_no = df[df["Play"] == "No"]
    
    # Features: Temp, Humidity, Windy
    new_data = np.array([45, 85, 2])
    
    # Calculate means and standard deviations (only for numeric columns)
    num_cols = ["Temp", "Humidity", "Windy"]
    
    yes_mean = df_yes[num_cols].mean()
    yes_std = df_yes[num_cols].std()
    
    no_mean = df_no[num_cols].mean()
    no_std = df_no[num_cols].std()
    
    yes_prob = gaussian_naive_bayes(new_data, yes_mean, yes_std)
    no_prob = gaussian_naive_bayes(new_data, no_mean, no_std)
    
    total_prob = yes_prob + no_prob
    if total_prob == 0:
        print("Total probability is zero. Unable to compute normalized probabilities.")
    else:
        print("--- GNB Scratch Probabilities ---")
        print("Yes Probability: ", yes_prob / total_prob)
        print("No Probability:  ", no_prob / total_prob)

if __name__ == "__main__":
    run_gaussian_nb_scratch()
