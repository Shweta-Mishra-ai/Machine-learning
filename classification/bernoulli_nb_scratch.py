"""Bernoulli Naive Bayes Classifier implemented from scratch.

This script demonstrates document tokenization, custom stop-words filtering,
and Bernoulli Naive Bayes feature matrix creation from text reviews.
"""

import os
import string
from collections import Counter
import numpy as np
import pandas as pd

def run_bernoulli_nb_scratch():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tsv_path = os.path.join(base_dir, "data", "Restaurant_Reviews.tsv")
    
    if not os.path.exists(tsv_path):
        print(f"Dataset not found: {tsv_path}")
        return

    # Load dataset
    dataset = pd.read_csv(tsv_path, delimiter="\t")
    df = pd.DataFrame(dataset.head())
    
    # Convert text to lowercase
    df["Review"] = df["Review"].apply(lambda x: x.lower())
    
    # Remove punctuations
    removed_punctuations = []
    for i in df["Review"]:
        n_str = ""
        for j in i:
            if j not in string.punctuation:
                n_str = n_str + j
        removed_punctuations.append(n_str)
        
    # Stop-words filtering
    stopwords = frozenset({"by", "the", "and", "it", "this", "was", "is", "on", "so", "were", "during", "just", "may"})
    clean_string_lst = []
    for i in removed_punctuations:
        n_str = ""
        for j in i.split():
            if j not in stopwords:
                n_str = n_str + " " + j
        clean_string_lst.append(n_str.strip())

    # Create word counts
    lst = [i.split() for i in clean_string_lst]
    preprocessed_string = [Counter(i) for i in lst]

    # Convert to feature DataFrame
    word_df = pd.DataFrame(preprocessed_string)
    word_df.fillna(value=0, inplace=True)
    
    # Fix numpy np.int deprecation bug
    word_df = word_df.astype(int)
    
    word_df["Target"] = df["Liked"].head()
    print("--- Bernoulli Naive Bayes Word Matrix ---")
    print(word_df)
    
    # Verify occurrences of 'loved' word
    if "loved" in word_df.columns:
        print("Loved & Liked:   ", len(word_df.loc[(word_df["loved"] == 1) & (word_df["Target"] == 1)]))
        print("Loved & Disliked:", len(word_df.loc[(word_df["loved"] == 1) & (word_df["Target"] == 0)]))
    else:
        print("Word 'loved' not found in sample headlines.")

if __name__ == "__main__":
    run_bernoulli_nb_scratch()
