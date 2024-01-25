class Stopword:
    """
    A class for handling stopwords in Creole Haitien text preprocessing.

    Methods:
        - load_stopwords: Loads and returns stopwords for Creole Haitien.
        - remove_stopwords(text): Removes stopwords from the given text.
        - is_stopword(word): Checks if a specific word is a stopword.
    """

    def __init__(self):
        """
        Initialize the Stopword object.
        """
        self.stopwords = self.load_stopwords()

    def load_stopwords(self):
        """
        Loads and returns stopwords for Creole Haitien.

        Returns:
            set: A set of stopwords.
        """
        with open('data\\creole_stopwords.txt', 'r', encoding='utf-8') as file:
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
        return ' '.join([word for word in text.split() if word not in self.stopwords])

    def is_stopword(self, word):
        """
        Checks if a specific word is a stopword.

        Parameters:
            word (str): The word to be checked.

        Returns:
            bool: True if the word is a stopword, False otherwise.
        """
        return word in self.stopwords