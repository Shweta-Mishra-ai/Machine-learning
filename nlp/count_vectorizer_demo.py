"""Text tokenization using CountVectorizer.

Fixes get_feature_names deprecations for sklearn compatibility.
"""

from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
import pandas as pd

def run_count_vectorizer():
    documents = [
        "Hello ||| This is first comment.....",
        "Python IS best Language!!!!",
        "Machine Learning is best lanGUage",
        "WOW that is awesome"
    ]
    
    cv = CountVectorizer(stop_words=list(ENGLISH_STOP_WORDS))
    X = cv.fit_transform(documents).toarray()
    
    # Corrected get_feature_names() to get_feature_names_out()
    df = pd.DataFrame(X, columns=cv.get_feature_names_out())
    print("--- Count Vectorizer Feature DataFrame ---")
    print(df)

if __name__ == "__main__":
    run_count_vectorizer()
