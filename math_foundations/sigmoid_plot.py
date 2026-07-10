"""Sigmoid Function definition and plotting script."""

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(a: np.ndarray) -> np.ndarray:
    """Compute the sigmoid function."""
    return 1 / (1 + np.exp(-a))

def run_sigmoid_plot():
    a = np.arange(-11, 11)
    b = sigmoid(a)
    print("--- Sigmoid values computed ---")
    print("a values:", a[8:13])
    print("sigmoid(a):", b[8:13])
    
    # Plot (Non-blocking)
    plt.figure(figsize=(6, 4))
    plt.plot(a, b, color="green")
    plt.grid(True)
    plt.title("Sigmoid Function")
    plt.show(block=False)
    plt.pause(2)
    plt.close()

if __name__ == "__main__":
    run_sigmoid_plot()
