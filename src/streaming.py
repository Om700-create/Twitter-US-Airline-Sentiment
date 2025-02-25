import tweepy
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables (API keys)
load_dotenv()

# Twitter API credentials
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Define a class to stream tweets
class TweetStreamListener(tweepy.StreamingClient):
    def __init__(self, output_file, max_tweets=100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output_file = output_file
        self.max_tweets = max_tweets
        self.tweet_count = 0
        self.tweets = []

    def on_tweet(self, tweet):
        # Extract relevant data from the tweet
        tweet_data = {
            "id": tweet.id,
            "text": tweet.text,
            "created_at": tweet.created_at,
            "user": tweet.user.screen_name,
            "location": tweet.user.location,
            "retweets": tweet.retweet_count,
            "likes": tweet.favorite_count,
        }
        self.tweets.append(tweet_data)
        self.tweet_count += 1

        # Stop streaming when max_tweets is reached
        if self.tweet_count >= self.max_tweets:
            self.disconnect()

    def on_error(self, status):
        print(f"Error: {status}")

    def on_disconnect(self):
        # Save tweets to a CSV file
        df = pd.DataFrame(self.tweets)
        df.to_csv(self.output_file, index=False)
        print(f"Saved {self.tweet_count} tweets to {self.output_file}")

# Set up streaming
if __name__ == "__main__":
    # Output file for tweets
    output_file = "data/raw/tweets.csv"

    # Create the data/raw directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Keywords to track
    keywords = ["data science", "machine learning", "AI", "artificial intelligence"]

    # Initialize the stream listener
    stream_listener = TweetStreamListener(output_file=output_file, max_tweets=100)

    # Start streaming
    print("Starting tweet stream...")
    stream_listener.filter(track=keywords)