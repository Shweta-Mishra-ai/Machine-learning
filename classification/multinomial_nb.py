"""Multinomial Naive Bayes text classification demo on 20newsgroups.

Classifies articles into news themes.
"""

from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
import matplotlib.pyplot as plt
import seaborn as sb

def run_multinomial_nb(sample_input: str = None):
    # Load news dataset
    dataset = fetch_20newsgroups()
    target_list = dataset.target_names
    
    X_train, X_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.2, random_state=False
    )
    
    tfidf_vector = TfidfVectorizer(stop_words=list(ENGLISH_STOP_WORDS))
    X_train_vec = tfidf_vector.fit_transform(X_train)
    X_test_vec = tfidf_vector.transform(X_test)
    
    model = MultinomialNB()
    model.fit(X_train_vec, y_train)
    
    print("Test Score: ", model.score(X_test_vec, y_test))
    
    if sample_input:
        sv = model.predict(tfidf_vector.transform([sample_input]))
        print(f"Input text: '{sample_input}'")
        print(f"Category: {target_list[sv[0]]}")

if __name__ == "__main__":
    run_multinomial_nb("Computer graphics card drivers for windows system")
