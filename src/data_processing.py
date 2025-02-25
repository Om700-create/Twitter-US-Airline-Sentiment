import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download NLTK resources
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("punkt_tab")

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Function to clean text
def clean_text(text):
    if isinstance(text, float):  # Handle NaN values
        return ""
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    # Remove special characters and numbers
    text = re.sub(r"\W", " ", text)
    text = re.sub(r"\d", " ", text)
    # Convert to lowercase
    text = text.lower()
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text

# Function to tokenize and lemmatize text
def tokenize_and_lemmatize(text):
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    return " ".join(tokens)

# Main function
def preprocess_data(input_file, output_file):
    # Load raw data
    df = pd.read_csv(input_file)

    # Handle missing values in the 'text' column
    df["text"] = df["text"].fillna("")  # Replace NaN with empty strings

    # Clean and preprocess text
    df["cleaned_text"] = df["text"].apply(clean_text)
    df["cleaned_text"] = df["cleaned_text"].apply(tokenize_and_lemmatize)

    # Save preprocessed data
    df.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")

# Run preprocessing
if __name__ == "__main__":
    # Input and output files
    input_file = "data/raw/reddit_posts.csv"
    output_file = "data/processed/cleaned_reddit_posts.csv"

    # Create the data/processed directory if it doesn't exist
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Preprocess data
    preprocess_data(input_file, output_file)