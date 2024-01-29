from pathlib import Path


class Stopword:
    """
    A class for handling stopwords in Creole Haitian text preprocessing.

    Methods:
        - load_stopwords(file_path): Loads and returns stopwords for Creole Haitien.
        - remove_stopwords(text): Removes stopwords from the given text.
        - is_stopword(word): Checks if a specific word is a stopword.
    """

    def __init__(self, stopwords_path='creolenltk/data/creole_stopwords.txt'):
        """
        Initialize the Stopword object.

        Parameters:
            stopwords_path (str): Path to the stopwords file.
        """
        self._stopwords = self.load_stopwords(stopwords_path)


    @property
    def stopwords(self):
        return self._stopwords


    def load_stopwords(self, file_path):
        """
        Loads and returns stopwords for Creole Haitien.

        Parameters:
            file_path (str): Path to the stopwords file.

        Returns:
            set: A set of stopwords.
        """
        file_path = Path(file_path).resolve()
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