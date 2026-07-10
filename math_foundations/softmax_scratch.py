"""Softmax Regression model implemented from scratch.

Merges the redundant logic from SOFTMAX_SCRATCH.txt and IRIS_SCRATCH.txt.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def one_hot_encode(y: np.ndarray) -> np.ndarray:
    """Convert integer classes to a one-hot representation."""
    y_enc = pd.get_dummies(y)
    return np.array(y_enc)

def net_input(X: np.ndarray, weight: np.ndarray, bias: np.ndarray) -> np.ndarray:
    """Compute the net input."""
    return np.dot(X, weight) + bias

def softmax(z: np.ndarray) -> np.ndarray:
    """Compute softmax probabilities."""
    return (np.exp(z.T) / np.sum(np.exp(z), axis=1)).T

def class_labels(cp: np.ndarray) -> np.ndarray:
    """Return index classification labels."""
    return cp.argmax(axis=1)

def cost_function(X: np.ndarray, w: np.ndarray, bias: np.ndarray, y: np.ndarray):
    """Compute log-loss cost and gradients."""
    N = X.shape[0]
    y_enc = one_hot_encode(y)
    z = net_input(X, w, bias)
    y_pred = softmax(z)
    
    # Prevent divide-by-zero or log(0)
    y_pred_clipped = np.clip(y_pred, 1e-9, 1 - 1e-9)
    
    cost = -(1 / N) * np.sum(y_enc * np.log2(y_pred_clipped))
    gradient = -(1 / N) * np.dot(X.T, (y_enc - y_pred))
    return cost, gradient

def run_softmax_scratch():
    # Toy datasets representing iris classification
    X = np.array([[5.1, 3.5], [6.4, 3.2], [6.9, 3.2], [5.6, 2.8]])
    y = np.array([0, 1, 2, 2])
    
    weight = np.array([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
    bias = np.array([0.1, 0.1, 0.1])
    
    # Train using simple Gradient Descent
    learning_rate = 0.1
    iterations = 100
    for _ in range(iterations):
        cost, gradient = cost_function(X, weight, bias, y)
        weight -= learning_rate * gradient
        
    z = net_input(X, weight, bias)
    cp = softmax(z)
    pred = class_labels(cp)
    
    print("--- Softmax Scratch Results ---")
    print("Actual labels:   ", y)
    print("Predicted labels:", pred)
    print("Accuracy:        ", np.mean(y == pred))

if __name__ == "__main__":
    run_softmax_scratch()
