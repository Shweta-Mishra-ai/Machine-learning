"""Word Counter scratch implementation.

Fixes np.int deprecation errors.
"""

import string
from collections import Counter
import pandas as pd
import numpy as np

def run_word_counter():
    documents = [
        "Hello ||| This is first comment.....",
        "Python IS best Language!!!!",
        "Machine Learning is best lanGUage",
        "WOW that is awesome"
    ]
    
    # Convert text to lowercase
    lower_case_documents = [doc.lower() for doc in documents]
    
    # Remove punctuations
    preprocessed_lst = []
    for doc in lower_case_documents:
        n_str = "".join(c for c in doc if c not in string.punctuation)
        preprocessed_lst.append(n_str)
        
    counter_lst = [doc.split() for doc in preprocessed_lst]
    word_vector_lst = [Counter(words) for words in counter_lst]
    
    df = pd.DataFrame(word_vector_lst)
    df.fillna(value=0, inplace=True)
    
    # Fixed np.int deprecation crash
    df = df.astype(int)
    print("--- Word Counter Output DataFrame ---")
    print(df)

if __name__ == "__main__":
    run_word_counter()
