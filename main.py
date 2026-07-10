"""Central entrypoint providing an interactive terminal menu for the repository.

Allows launching games, machine learning models, custom CLI scripts, and
running the unit test suite.
"""

import os
import sys
import subprocess

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner():
    print("=" * 60)
    print("      __  ___      __    _             __                 ")
    print("     /  |/  /___ _/ /_  (_)___  ___   / /   ___  ___ _ ____")
    print("    / /|_/ / __ `/ __ \\/ / __ \\/ _ \\ / /   / _ \\/ _ `// __/")
    print("   / /  / / /_/ / / / / / / / /  __// /___/  __/ /_/ // /   ")
    print("  /_/  /_/\\__,_/_/ /_/_/_/ /_/\\___//_____/\\___/\\__,_//_/    ")
    print("                                                            ")
    print("             PRODUCTION-GRADE MACHINE LEARNING SUITE        ")
    print("=" * 60)

def run_script(relative_path: str):
    """Run a Python script in a separate subprocess."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, relative_path.replace("/", os.sep))
    
    if not os.path.exists(script_path):
        print(f"Error: Script not found at {script_path}")
        input("\nPress Enter to return...")
        return
        
    print(f"\n>>> Executing {relative_path}...\n")
    try:
        # Run using current python interpreter
        result = subprocess.run([sys.executable, script_path], check=False)
        print(f"\n>>> Execution finished with exit code {result.returncode}.")
    except Exception as e:
        print(f"\n>>> Failed to run script: {e}")
        
    input("\nPress Enter to return to menu...")

def run_tests():
    """Run the automated test suite."""
    print("\n>>> Launching Automated Unit Test Suite...\n")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        result = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests"], cwd=base_dir, check=False)
        print(f"\n>>> Test Suite finished with exit code {result.returncode}.")
    except Exception as e:
        print(f"\n>>> Failed to run tests: {e}")
    input("\nPress Enter to return...")

def category_menu(category_name: str, scripts: dict):
    """Render a submenu for a specific category of scripts."""
    while True:
        clear_screen()
        print("=" * 60)
        print(f" {category_name.upper()} SCRIPTS")
        print("=" * 60)
        
        choices = sorted(scripts.keys())
        for idx, key in enumerate(choices, 1):
            print(f"  {idx}. {key}")
        print("  0. Back to Main Menu")
        print("=" * 60)
        
        try:
            choice = int(input("Select an option: "))
            if choice == 0:
                break
            if 1 <= choice <= len(choices):
                key = choices[choice - 1]
                run_script(scripts[key])
            else:
                print("Invalid choice. Try again.")
                time.sleep(1)
        except ValueError:
            print("Please enter a valid integer.")
            time.sleep(1)

def main():
    # Define script libraries
    games = {
        "Snakes and Ladders": "games/snakes_and_ladders.py",
        "Russian Roulette (Josephus)": "games/russian_roulette.py"
    }
    
    cli_tools = {
        "Movie Recommendation Engine": "cli/movie_recommendation.py",
        "Preserved Practice Basics": "cli/practice_basics.py",
        "Secure SMTP Email Sender Demo": "utils/email_sender.py"
    }

    classification = {
        "Bernoulli Naive Bayes (Scratch)": "classification/bernoulli_nb_scratch.py",
        "Bernoulli Naive Bayes (scikit-learn)": "classification/bernoulli_nb_sklearn.py",
        "Gaussian Naive Bayes (Scratch)": "classification/gaussian_nb_scratch.py",
        "K-Nearest Neighbors (Scratch)": "classification/knn_scratch.py",
        "Multinomial Naive Bayes (News)": "classification/multinomial_nb.py",
        "Digit Recognition (Logistic Regression)": "classification/digit_recognize.py",
        "Breast Cancer Classification (SVM) [NEW]": "classification/breast_cancer_classification.py",
        "Diabetes Diagnostic Model (Random Forest) [NEW]": "classification/diabetes_classification.py",
        "HR Employee Retention Predictor (Random Forest) [NEW]": "classification/hr_employee_retention.py"
    }

    regression = {
        "Simple Linear Regression (House Prices)": "regression/simple_linear_regression.py",
        "Multiple Linear Regression (House Prices)": "regression/multiple_linear_regression.py",
        "Flash vs Arrow Viewers Comparison": "regression/flash_vs_arrow_regression.py",
        "Polynomial Regression (Salaries)": "regression/polynomial_regression.py",
        "Melbourne House Price Advanced Regression [NEW]": "regression/melbourne_house_price.py"
    }

    clustering_pca = {
        "Hierarchical Clustering (Mall Customers)": "clustering_pca/hierarchical_clustering.py",
        "Principal Component Analysis (PCA Scratch)": "clustering_pca/pca_scratch.py"
    }

    nlp = {
        "Count Vectorizer Bag-of-Words Demo": "nlp/count_vectorizer_demo.py",
        "Twitter Sentiment Analyzer (Tweepy & VADER)": "nlp/twitter_sentiments.py",
        "VADER Sentiment Intensity Demo": "nlp/vader_sentiments.py",
        "Document Word Counter (Scratch)": "nlp/word_counter_scratch.py"
    }

    model_tuning = {
        "GridSearchCV Hyperparameter Tuning": "model_tuning/grid_search.py",
        "K-Fold & Stratified Cross-Validation": "model_tuning/k_fold_cv.py",
        "Label Encoder & One-Hot Encoder Demo": "model_tuning/label_encoder_ohe.py",
        "Model Persistence Serialization (Pickle & Joblib)": "model_tuning/model_persistence.py",
        "Min-Max Scaling Normalization": "model_tuning/min_max_scaling.py",
        "Train-Test Validation Split": "model_tuning/train_test_split.py"
    }

    math_foundations = {
        "Sigmoid Activation Plotter": "math_foundations/sigmoid_plot.py",
        "Softmax Regression (Scratch)": "math_foundations/softmax_scratch.py",
        "Vector Dot Product Calculation": "math_foundations/vector_dot.py"
    }

    while True:
        clear_screen()
        print_banner()
        print("  1. Play Interactive Games")
        print("  2. Run Custom CLI Tools")
        print("  3. Classification Models")
        print("  4. Regression Models")
        print("  5. Clustering & Principal Component Analysis")
        print("  6. Natural Language Processing (NLP) Demos")
        print("  7. Model Tuning & Preprocessing Demos")
        print("  8. Mathematical Foundations")
        print("  9. Run Automated Test Suite (discover tests/)")
        print("  0. Exit")
        print("=" * 60)
        
        try:
            choice = input("Select an option: ").strip()
            if choice == "0":
                print("\nGoodbye!")
                break
            elif choice == "1":
                category_menu("Games", games)
            elif choice == "2":
                category_menu("CLI Tools", cli_tools)
            elif choice == "3":
                category_menu("Classification", classification)
            elif choice == "4":
                category_menu("Regression", regression)
            elif choice == "5":
                category_menu("Clustering & PCA", clustering_pca)
            elif choice == "6":
                category_menu("NLP Demos", nlp)
            elif choice == "7":
                category_menu("Model Tuning & Preprocessing", model_tuning)
            elif choice == "8":
                category_menu("Mathematical Foundations", math_foundations)
            elif choice == "9":
                run_tests()
            else:
                print("Invalid option. Please try again.")
                import time; time.sleep(1)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
