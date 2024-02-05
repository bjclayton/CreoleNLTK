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
        "fin": "fini",
        "sot": "soti",
        "k": "ki",
        "al": "ale",
        "konn": "konnen",
        "kab": "kapab",
        "lap": "li ap",
        "paka": "pa kapab",
        "jan": "kijan",
        "diw": "di ou",
        "poum": "pou mwen",
        "yok": "yo ki",
        "yap": "yo ap",
        "tap": "te ap",
        "kap": "ki ap",
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
                pattern = re.compile(r'\b' + re.escape(key) + r'\b', re.IGNORECASE)
                text = re.sub(pattern, value, text)
            return text
        else:
            return text
