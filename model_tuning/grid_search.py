"""Hyperparameter tuning using GridSearchCV on Iris dataset."""

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

def run_grid_search():
    dataset = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.2, random_state=False
    )
    
    params = [{"n_neighbors": list(range(1, 15)), "metric": ["euclidean", "manhattan"]}]
    gs_cv = GridSearchCV(KNeighborsClassifier(), param_grid=params)
    gs_cv.fit(X_train, y_train)
    
    print("--- GridSearchCV Complete ---")
    print("Best Parameters Found:", gs_cv.best_params_)
    print("Best Cross-Validation Score:", gs_cv.best_score_)

if __name__ == "__main__":
    run_grid_search()
