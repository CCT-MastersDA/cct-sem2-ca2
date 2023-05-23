"""
text_processor.py

This file contains the definition of the TextProcessor class,
which was implemented to handle the text processing for the ML analysis.

This class was implemented as a module to avoid code duplicate and for easier reference.
"""
# importing modules
from textblob import TextBlob
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import re
import string

# list of sentiment labels
sentiment_lst = ['negative', 'neutral', 'positive']

class TextProcessor:
    """
    Helper class to perform text processing using NLP techniques.
    """
    def __init__(self):
        """
        The constructor for TextProcessor class.
        """
        return

    @staticmethod
    def get_sentiment(text):
        """
        Auxiliary method to extract the sentiment from the input text.

        Parameters:
            text (str): String to be processed.
        Returns:
            sentiment (str): negative, positive or neutral value.
        """
        res = TextBlob(text).sentiment.polarity
        if res < 0:
          return sentiment_lst[0]
        elif res > 0:
          return sentiment_lst[2]
        return sentiment_lst[1]

    @staticmethod
    def process_text(text, use_stemmer=False, use_lemmatizer=False):
        """
        Method responsible to execute all text processing steps.

        It converts text to lower case, removes special characters and urls,
        filters out stop words, tokenize and perform stemmer/lemmatizer as per parameters.

        Parameters:
            text       (str): Text to be cleaned.
            use_stemmer    (bol): Flag to indicate if processing should include text stemmer.
            use_lemmatizer (bol): Flag to indicate if processing should include text lemmatizer.
        Returns:
            text (str): Cleaned text.
        """
        text = TextProcessor.clean_text(text)
        tokens = TextProcessor.get_tokens(text)
        filtered_words = TextProcessor.filter_stop_words(tokens)

        if use_stemmer:
            filtered_words = TextProcessor.apply_stemmer(filtered_words)

        if use_lemmatizer:
            filtered_words = TextProcessor.apply_lemmatizer(filtered_words)

        return " ".join(filtered_words)

    @staticmethod
    def clean_text(text):
        """
        Auxiliary method to remove special characters, urls and ponctuations from the text.

        Parameters:
            text (str): String to be cleaned.
        Returns:
            text (str): Clened text.
        """
        # convert to lower case
        text = text.lower()
        # remove urls
        text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
        # remove user @ references and '#' from text
        text = re.sub(r'\@\w+|\#','', text)
        # removing special chars
        text = re.sub('[^a-zA-Z]', ' ', text)
        # remove punctuations
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text

    @staticmethod
    def get_tokens(text):
        """
        Auxiliary method to extract a vector of tokens from the input text.

        Parameters:
            text (str): String to be tokenized.
        Returns:
            tokens ([]): Tokenized words.
        """
        return word_tokenize(text)

    @staticmethod
    def filter_stop_words(tokens=[]):
        """
        Auxiliary method to filter out stop words.

        Parameters:
            tokens ([]): String array to be filtered.
        Returns:
            tokens ([]): Filtered words.
        """
        stop_words = set(stopwords.words('english'))
        filtered_words = [w for w in tokens if not w in stop_words]
        return filtered_words

    @staticmethod
    def apply_stemmer(tokens=[]):
        """
        Auxiliary method to apply Porter Stemmer to the tokens list.

        Parameters:
            tokens ([]): String array to be processed.
        Returns:
            stemmed_words ([]): Stemmed words.
        """
        ps = PorterStemmer()
        stemmed_words = [ps.stem(w) for w in tokens]
        return stemmed_words

    @staticmethod
    def apply_lemmatizer(tokens=[], part_of_speech='a'):
        """
        Auxiliary method to apply Word Net Lemmatizer to the tokens list.

        Parameters:
            tokens ([]): String array to be processed.
        Returns:
            lemma_words ([]): Lemmatized words.
        """
        lemmatizer = WordNetLemmatizer()
        lemma_words = [lemmatizer.lemmatize(w, pos=part_of_speech) for w in tokens]
        return lemma_words