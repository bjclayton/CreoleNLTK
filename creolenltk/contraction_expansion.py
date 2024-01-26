import re

class ContractionToExpansion:
    """
    A class for expanding contractions in Creole Haitian text.

    Methods:
    - expand_contractions(text): Expands contractions in the input text.
    """

    CONTRACTIONS_MAPPING = {
        "m": "mwen",
        "mw": "mwen",
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
        "paka": "pa kapab",
        "al": "ale",
        "jan": "kijan",
        "diw": "di ou",
        "poum": "pou mwen",
        "yok": "yo ki",
        "yap": "yo ap"
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
        if isinstance(text, str):
            text = text.replace("'", " ")
            for key, value in ContractionToExpansion.CONTRACTIONS_MAPPING.items():
                text = re.sub(r'\b' + re.escape(key.lower()) + r'\b', value, text)
            return text
        else:
            return text