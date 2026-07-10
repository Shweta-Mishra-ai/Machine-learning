"""K-Fold Cross-Validation evaluation script.

Applies cross-validation to KNN, Gaussian NB, and Decision Trees.
"""

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score
import numpy as np

def get_model_score(model, X_train, X_test, y_train, y_test) -> float:
    model.fit(X_train, y_train)
    return model.score(X_test, y_test)

def run_k_fold_cv():
    # Simple KFold Split Demo
    kf = KFold(n_splits=3)
    print("--- KFold splits index demo ---")
    for train_set, test_set in kf.split(list(range(1, 10))):
        print(f"Train indices: {train_set} | Test indices: {test_set}")

    dataset = load_iris()
    X = dataset.data
    y = dataset.target
    
    knn_score = []
    gnb_score = []
    dtc_score = []
    
    skf = StratifiedKFold(n_splits=3)
    for train_idx, test_idx in skf.split(X, y):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        
        knn_score.append(get_model_score(KNeighborsClassifier(), X_train, X_test, y_train, y_test))
        gnb_score.append(get_model_score(GaussianNB(), X_train, X_test, y_train, y_test))
        dtc_score.append(get_model_score(DecisionTreeClassifier(), X_train, X_test, y_train, y_test))
        
    print("\n--- Stratified K-Fold Mean Scores ---")
    print("KNN K-Fold Mean: ", np.mean(knn_score))
    print("GNB K-Fold Mean: ", np.mean(gnb_score))
    print("DTC K-Fold Mean: ", np.mean(dtc_score))

if __name__ == "__main__":
    run_k_fold_cv()
