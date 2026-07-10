"""Twitter Sentiment Analysis.

Includes credentials validation to prevent immediate crashes and guides the user.
"""

import tweepy
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def run_twitter_sentiments(search_text: str = "Machine Learning"):
    # Tweepy API credentials placeholder
    consumer_key = ""
    consumer_secret_key = ""
    access_token = ""
    access_secret_key = ""
    
    print("--- Twitter Sentiment Analyzer ---")
    
    if not all([consumer_key, consumer_secret_key, access_token, access_secret_key]):
        print("Twitter credentials not set. Simulating analysis with mock search tweets.")
        # Fallback offline simulation
        mock_tweets = [
            f"I absolutely love {search_text}! It is the future.",
            f"This new tool for {search_text} is so-so, not that great.",
            f"Learning {search_text} is incredibly hard and frustrating."
        ]
        
        vader = SentimentIntensityAnalyzer()
        for idx, text in enumerate(mock_tweets, 1):
            print(f"Mock Tweet {idx}: '{text}'")
            print("  VADER Polarity Scores:", vader.polarity_scores(text))
            print("  TextBlob Sentiment:   ", TextBlob(text).sentiment)
        return

    try:
        # Modernized tweepy authentication
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
        auth.set_access_token(access_token, access_secret_key)
        tweeter_api = tweepy.API(auth)
        
        # Updated search method for compatibility
        tweets = tweeter_api.search_tweets(search_text)
        vader = SentimentIntensityAnalyzer()
        for t in tweets:
            print("Tweet text:", t.text)
            print("VADER Scores:", vader.polarity_scores(t.text))
    except Exception as e:
        print("Authentication / Network Error during Twitter API search:", e)

if __name__ == "__main__":
    run_twitter_sentiments()
