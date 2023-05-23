"""
constants.py

This file contains the constants used in the Jupyter notebooks of this project.

They are defined in a separate file to avoid code duplicate and for easier reference.
"""
# importing modules
import os
import warnings
from pathlib import Path
from os.path import isfile, join, abspath

# path to the users directory
HOME_DIR = str(Path.home())

# path to the current directory
CURR_PATH = abspath(os.getcwd())

# path to the images folder
IMAGES_FOLDER = join(CURR_PATH, 'images')

# path to input dataset folder
DATASETS_FOLDER = join(CURR_PATH, 'datasets')

# path to the tweets dataset raw
TWEETS_DS_RAW = join(DATASETS_FOLDER, 'tweets_raw.csv')

# path to the tweets dataset after pre-processing
TWEETS_SENT = join(DATASETS_FOLDER, 'tweets_sentiment.csv')

# max number of features for the vectorizer strategy
MAX_FEATURES = 5000

# ignore warnings
warnings.filterwarnings('ignore')

# image files
TWEETS_WORD_CLOUD = 'tweets-word-cloud.png'