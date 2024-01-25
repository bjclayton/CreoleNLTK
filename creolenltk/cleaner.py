import re
from bs4 import BeautifulSoup

class Cleaner():
    """
        A class for performing various text cleaning operations.

        Methods:
        - normalize_whitespace(text): Normalize whitespace in the text.
        - remove_html_tags(text): Remove HTML tags from the text.
        - remove_special_characters(text): Remove special characters, punctuation, or symbols from the text.
        - remove_numbers(text): Remove numerical digits from the text.
        - clean_text(text, lowercase=True): Perform a comprehensive text cleaning.
        """

    def __init__(self):
        """
        Initialize the Cleaner object.
        """
        pass


    @staticmethod
    def normalize_whitespace(self, text):
        """
        Normalize whitespace in the text by replacing consecutive spaces with a single space.

        Parameters:
        - text (str): The input text.

        Returns:
        - str: Text with normalized whitespace.
        """
        return ' '.join(text.split())
    

    @staticmethod
    def remove_html_tags(self, text):
        """
        Remove HTML tags from the text.

        Parameters:
        - text (str): The input text containing HTML tags.

        Returns:
        - str: Text with HTML tags removed.
        """
        soup = BeautifulSoup(text, 'html.parser')
        return soup.get_text()


    @staticmethod
    def remove_special_characters(self, text):
        """
        Remove special characters, punctuation, or symbols from the text.

        Parameters:
        - text (str): The input text.

        Returns:
        - str: Text with special characters removed.
        """
        return self.normalize_whitespace(re.sub(r'[^\w ]+', '', text))
    

    @staticmethod
    def remove_numbers(self, text):
        """
        Remove numerical digits from the text.

        Parameters:
        - text (str): The input text.

        Returns:
        - str: Text with numbers removed.
        """
        return self.normalize_whitespace(re.sub(r'\d+', '', text))
    

    @staticmethod
    def clean_text(self, text, lowercase=True):
        """
        Perform a comprehensive text cleaning.

        Parameters:
        - text (str): The input text.
        - lowercase (bool): Whether to convert the text to lowercase (default is True).

        Returns:
        - str: Cleaned text.
        """
        cleaned_html = self.remove_html_tags(text)
        cleaned_special_chars = self.remove_special_characters(cleaned_html)
        cleaned_text = self.remove_numbers(cleaned_special_chars)

        if lowercase:
            return cleaned_text.lower()
        else:
            return cleaned_text