import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon
nltk.download("vader_lexicon")

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to predict sentiment
def predict_sentiment(text):
    if isinstance(text, float):  # Handle NaN values
        return "neutral"  # Default to neutral for missing text
    # Get sentiment scores
    scores = analyzer.polarity_scores(text)
    # Determine sentiment based on compound score
    if scores["compound"] >= 0.05:
        return "positive"
    elif scores["compound"] <= -0.05:
        return "negative"
    else:
        return "neutral"

# Main function
def analyze_sentiment(input_file, output_file):
    # Load cleaned data
    df = pd.read_csv(input_file)

    # Handle missing values in the 'cleaned_text' column
    df["cleaned_text"] = df["cleaned_text"].fillna("")  # Replace NaN with empty strings

    # Predict sentiment for each post
    df["sentiment"] = df["cleaned_text"].apply(predict_sentiment)

    # Save results
    df.to_csv(output_file, index=False)
    print(f"Sentiment analysis results saved to {output_file}")

# Run sentiment analysis
if __name__ == "__main__":
    # Input and output files
    input_file = "data/processed/cleaned_reddit_posts.csv"
    output_file = "data/processed/reddit_posts_with_sentiment.csv"

    # Analyze sentiment
    analyze_sentiment(input_file, output_file)