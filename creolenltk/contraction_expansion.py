import re

class ContractionToExpansion:
    """
    A class for expanding contractions in Creole Haitian text.

    Methods:
    - expand_contractions(text): Expands contractions in the input text.
    """

    CONTRACTIONS_MAPPING = {
        "m": "mwen",
        "mw": "mwwen",
        "n": "nou",
        "ka": "kapab",
        "l": "li",
        "pot": "te poko",
        "t": "te",
        "w": "ou",
        "pral": "prale",
        "fin": "fini",
        "sot": "soti",
        "k": "ki",
        "al": "ale",
        "konn": "konnen",
        "kab": "kapab",
        "lap": "li ap",
        "pap": "pa",
        "al": "ale",
        "jan": "kijan"
    }

    @staticmethod
    def expand_contractions(text):
        """
        Expands contractions in the input text.

        Parameters:
        text (str): Input text containing contractions.

        Returns:
        str: Text with contractions expanded.
        """
        text = text.replace("'", " ")

        if isinstance(text, str):
            for key, value in ContractionToExpansion.CONTRACTIONS_MAPPING.items():
                text = re.sub(r'\b' + re.escape(key) + r'\b', value, text)
            return text
        else:
            return text