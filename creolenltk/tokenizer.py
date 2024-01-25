import nltk
import re
from contraction_expansion import ContractionToExpansion

class Tokenizer:
    """
    The Tokenizer class provides functionality for tokenizing text.

    Methods:
        word_tokenize(text): Tokenize the input text into a list of words.
    """

    @staticmethod
    def word_tokenize(text, expand_contractions=False):
        """
        Tokenize the input text into a list of words.

        Parameters:
            text (str): The input text to be tokenized.
            expand_contractions (bool, optional): If True, expands contractions in the text. Default is False.

        Returns:
            list: A list of tokens (words) extracted from the input text.
        """
        text = re.sub(r"[^\w\s']", '', text)

        if(expand_contractions):
            text = ContractionToExpansion.expand_contractions(text)

        return  nltk.word_tokenize(text)