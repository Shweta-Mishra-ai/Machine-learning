"""Bernoulli Naive Bayes Classifier using scikit-learn.

Classifies messages from a spam dataset and optionally triggers audio alerts.
"""

import os
import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sb

def run_bernoulli_nb_sklearn():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "spam.csv")
    
    if not os.path.exists(csv_path):
        print(f"Dataset not found: {csv_path}")
        return

    df = pd.read_csv(csv_path, engine="python")
    df.dropna(axis=1, inplace=True)
    df["v1"] = df["v1"].map({"spam": 0, "ham": 1})
    
    X_train, X_test, y_train, y_test = train_test_split(
        df["v2"], df["v1"], test_size=0.2, random_state=False
    )
    
    count = CountVectorizer(stop_words=list(ENGLISH_STOP_WORDS))
    X_train_vec = count.fit_transform(X_train)
    X_test_vec = count.transform(X_test)
    
    model = BernoulliNB()
    model.fit(X_train_vec, y_train)
    
    y_pred = model.predict(X_test_vec)
    cm = confusion_matrix(y_test, y_pred)
    
    print("TEST SCORE:", model.score(X_test_vec, y_test))
    
    # Try prediction on spam sample
    test_msg = "Free entry in 2 a wkly comp to win FA Cup"
    sv = model.predict(count.transform([test_msg]))
    if sv[0] == 1:
        print(f"Message: '{test_msg}' -> HAM")
    else:
        print(f"Message: '{test_msg}' -> SPAM")
        # Optional sound playback wrapped safely to prevent crashes
        try:
            import playsound
            sound_path = os.path.join(base_dir, "data", "Intruder Alert.mp3")
            if not os.path.exists(sound_path):
                # Search in original place
                sound_path = os.path.join(base_dir, "Misc-Practice", "Intruder Alert.mp3")
            if os.path.exists(sound_path):
                playsound.playsound(sound_path)
        except Exception as e:
            print("Spam alert triggered (sound playback skipped).")

    # Plot Confusion Matrix (Non-blocking)
    plt.figure(figsize=(6, 4))
    sb.heatmap(data=cm, annot=True, fmt="d", xticklabels=["spam", "ham"], yticklabels=["spam", "ham"])
    plt.title("Confusion Matrix")
    plt.show(block=False)
    plt.pause(2)
    plt.close()

if __name__ == "__main__":
    run_bernoulli_nb_sklearn()
