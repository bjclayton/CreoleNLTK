from pathlib import Path


class Stopword:
    """
    A class for handling stopwords in Creole Haitian text preprocessing.

    Methods:
        - load_stopwords(): Loads and returns stopwords for Creole Haitien.
        - remove_stopwords(text): Removes stopwords from the given text.
        - is_stopword(word): Checks if a specific word is a stopword.
    """

    def __init__(self):
        """
        Initialize the Stopword object.
        """
        self._stopwords = self.load_stopwords()

    @property
    def stopwords(self):
        return self._stopwords

    def load_stopwords(self):
        """
        Loads and returns stopwords for Creole Haitien.

        Returns:
            set: A set of stopwords.
        """
        file_path = Path(__file__).parent / 'data' / 'creole_stopwords.txt'
        with open(file_path, encoding='utf-8') as file:
            stopwords = {word.strip('\n') for word in file}
        return stopwords

    def remove_stopwords(self, text):
        """
        Removes stopwords from the given text.

        Parameters:
            text (str): The input text.

        Returns:
            str: The text with stopwords removed.
        """
        return ' '.join([word for word in text.split() if str(word).lower() not in self.stopwords])

    def is_stopword(self, word):
        """
        Checks if a specific word is a stopword.

        Parameters:
            word (str): The word to be checked.

        Returns:
            bool: True if the word is a stopword, False otherwise.
        """
        return word.lower() in self.stopwords
