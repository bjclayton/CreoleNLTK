import nltk
import re
from .contraction_expansion import ContractionToExpansion


class Tokenizer:
    """
    The Tokenizer class provides functionality for tokenizing text.

    Methods:
        - word_tokenize(text, expand_contractions, lowercase): Tokenize the input text into a list of words.
    """

    @staticmethod
    def word_tokenize(text, expand_contractions=False, lowercase=True):
        """
        Tokenize the input text into a list of words.

        Parameters:
            - text (str): The input text to be tokenized.
            - expand_contractions (bool, optional): If True, expands contractions in the text. Default is False.
            - lowercase (bool, optional): Whether to convert the text to lowercase (default is True).

        Returns:
            list: A list of tokens (words) extracted from the input text.
        """
        if text is None or str(text) == '':
            return []

        text = re.sub(r"[^\w\s']", '', text)

        if expand_contractions:
            text = ContractionToExpansion.expand_contractions(text)

        if lowercase:
            text = text.lower()

        return nltk.word_tokenize(text)
