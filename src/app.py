import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

# Load the sentiment analysis results
df = pd.read_csv("data/processed/reddit_posts_with_sentiment.csv")

# Set up the Streamlit app
st.title("Real-Time Sentiment Analysis Dashboard")
st.write("This dashboard visualizes the sentiment analysis results for Reddit posts.")

# 1. Sentiment Distribution
st.header("Sentiment Distribution")
sentiment_counts = df["sentiment"].value_counts()
st.bar_chart(sentiment_counts)

# 2. Word Clouds
st.header("Word Clouds")

# Function to generate a word cloud
def generate_wordcloud(text, title):
    if not text.strip():
        st.write(f"No words available to generate a word cloud for {title}.")
        return
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.title(title)
    plt.axis("off")
    st.pyplot(plt)

# Combine all text for each sentiment
positive_text = " ".join(str(text) for text in df[df["sentiment"] == "positive"]["cleaned_text"] if isinstance(text, str))
negative_text = " ".join(str(text) for text in df[df["sentiment"] == "negative"]["cleaned_text"] if isinstance(text, str))

# Display word clouds
st.subheader("Positive Posts")
generate_wordcloud(positive_text, "Word Cloud for Positive Posts")

st.subheader("Negative Posts")
generate_wordcloud(negative_text, "Word Cloud for Negative Posts")

# 3. Most Common Words
st.header("Most Common Words")

# Function to get the most common words
def get_most_common_words(text, n=10):
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(n)

# Display most common words
st.subheader("Positive Posts")
st.write(get_most_common_words(positive_text))

st.subheader("Negative Posts")
st.write(get_most_common_words(negative_text))

st.subheader("Neutral Posts")
st.write("No words available for neutral posts.")