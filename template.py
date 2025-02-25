import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of files and folders to create
list_of_files = [
    # Data directories
    "data/raw/tweets.csv",  # Raw social media data (e.g., tweets)
    "data/processed/__init__.py",  # Processed data placeholder
    "data/processed/cleaned_tweets.csv",  # Cleaned and preprocessed data
    "data/external/__init__.py",  # External data (e.g., sentiment lexicons)
    "data/interim/__init__.py",  # Intermediate data (e.g., tokenized text)

    # Notebooks for exploration and analysis
    "notebooks/01_data_exploration.ipynb",  # Exploratory Data Analysis (EDA)
    "notebooks/02_sentiment_analysis.ipynb",  # Sentiment analysis and visualization
    "notebooks/03_model_training.ipynb",  # Model training and evaluation
    "notebooks/04_real_time_monitoring.ipynb",  # Real-time sentiment monitoring

    # Source code for the project
    "src/__init__.py",  # Package initialization
    "src/data_processing.py",  # Data cleaning and preprocessing functions
    "src/feature_engineering.py",  # Feature engineering (e.g., TF-IDF, embeddings)
    "src/model.py",  # Model definition and training (e.g., BERT, LSTM)
    "src/utils.py",  # Utility functions (e.g., logging, visualization)
    "src/app.py",  # Main application for real-time sentiment analysis
    "src/api.py",  # API for real-time sentiment prediction
    "src/streaming.py",  # Streaming data from social media APIs

    # Configuration and environment files
    "config/config.yaml",  # Configuration file for hyperparameters and paths
    "requirements.txt",  # List of dependencies for the project
    "setup.py",  # Setup script for packaging the project
    ".env",  # Environment variables (e.g., API keys)

    # Documentation and project management
    "README.md",  # Project overview and documentation
    "LICENSE",  # License file for the project (e.g., MIT License)
    ".gitignore",  # Files/folders to ignore in Git
    "docs/overview.md",  # Project documentation
    "tests/__init__.py",  # Unit tests for the project
    "tests/test_data_processing.py",  # Tests for data processing
    "tests/test_model.py",  # Tests for model functionality
]

# Create files and folders
for filepath in list_of_files:
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Create empty files if they don't exist or are empty
    if not os.path.exists(filepath) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already created")