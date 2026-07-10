"""VADER Sentiment Intensity Analyzer demo."""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def run_vader_sentiments(text: str = "This is a great library! I love it."):
    sentiments = SentimentIntensityAnalyzer()
    score = sentiments.polarity_scores(text)
    print("--- VADER Sentiment Scores ---")
    print(f"Input text: '{text}'")
    print("Scores:    ", score)

if __name__ == "__main__":
    run_vader_sentiments()
