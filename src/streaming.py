import praw
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Reddit API credentials
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Authenticate with Reddit API
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
)

# Function to collect posts from a subreddit
def collect_posts(subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for post in subreddit.new(limit=limit):
        post_data = {
            "id": post.id,
            "title": post.title,
            "text": post.selftext,
            "author": post.author.name if post.author else "deleted",
            "upvotes": post.score,
            "created_at": post.created_utc,
            "url": post.url,
        }
        posts.append(post_data)

    return posts

# Save posts to a CSV file
def save_posts(posts, output_file):
    df = pd.DataFrame(posts)
    df.to_csv(output_file, index=False)
    print(f"Saved {len(posts)} posts to {output_file}")

# Main function
if __name__ == "__main__":
    # Output file for posts
    output_file = "data/raw/reddit_posts.csv"

    # Create the data/raw directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Subreddit to collect posts from
    subreddit_name = "dataisbeautiful"  # Replace with your desired subreddit

    # Collect posts
    print(f"Collecting posts from r/{subreddit_name}...")
    posts = collect_posts(subreddit_name, limit=100)

    # Save posts to CSV
    save_posts(posts, output_file)