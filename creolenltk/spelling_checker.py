import re
from collections import Counter
import string
from pathlib import Path

class SpellingChecker:
    """
    A class for correcting spelling errors in text based on: Peter Norvig, "How to Write a Spelling Corrector", http://norvig.com/spell-correct.html

    Methods:
        - _load(file_path): Load words from the given file.
        - _extract_words(text): Extract words from the given text.
        - _probability(word): Return the probability of the given word.
        - suggests(word): Return the most probable correction for the given word.
        - _candidates(word): Generate possible spelling corrections for the given word.
        - _known(words): Filter the list of words to include only those present in the words list.
        - _edits1(word): Generate all possible edits at a distance of 1 from the given word.
        - _edits2(word): Generate all possible edits at a distance of 2 from the given word.
    """

    def __init__(self, words_file='creolenltk/data/creole_words.txt'):
        """
        Initialize the spelling checker with a words.

        Parameters:
            words_file (str or Path): Path to the words file.
        """
        self._WORDS = self._load(words_file)


    def _load(self, file_path):
        """
        Load words from the given file.

        Parameters:
            file_path (str or Path): Path to the words file.

        Returns:
            Counter: A counter of words.
        """
        file_path = Path(file_path).resolve()
        with open(file_path, encoding='utf-8') as file:
            words = file.read()
        return Counter(self._extract_words(words))


    def _extract_words(self, text):
        """
        Extract words from the given text.

        Parameters:
            text (str): Input text.

        Returns:
            list: List of words extracted from the text.
        """
        return re.findall(r'\w+', text.lower())


    def _probability(self, word):
        """
        Return the probability of the given word.

        Parameters:
            word (str): The word for which probability is calculated.

        Returns:
            float: The probability of the word.
        """
        total_words = sum(self._WORDS.values())
        return self._WORDS[word] / total_words
    

    def suggests(self, word):
        """
        Return the most probable correction for the given word.

        Parameters:
            word (str): The word to be corrected.

        Returns:
            str: The most probable correction for the word.
        """
        print(self._candidates(word))
        return max(self._candidates(word), key=self._probability)


    def _candidates(self, word):
        """
        Generate possible spelling corrections for the given word.

        Parameters:
            word (str): The word for which corrections are generated.

        Returns:
            list: List of possible corrections for the word.
        """
        if len(word) == 1 or word in string.punctuation or word in string.whitespace:
            return [word]
        if word.replace(".", "").isdigit() or word.replace(",", "").isdigit():
            return [word]
        
        return (self._known([word]) or
                self._known(self._edits1(word)) or
                self._known(self._edits2(word)) or
                [word])
    

    def _known(self, words):
        """
        Filter the list of words to include only those present in the words list.

        Parameters:
            words (list): List of words to be filtered.

        Returns:
            set: Set of known words.
        """
        return set(w for w in words if w in self._WORDS)


    def _edits1(self, word):
        """
        Generate all possible edits at a distance of 1 from the given word.

        Parameters:
            word (str): The word for which edits are generated.

        Returns:
            set: Set of possible edits.
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        # alpha = "a an b ch d e en è f g h j i k l m n ng o ò on ou oun p r s t ui v w y z"
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [a + b[1:] for a, b in splits if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
        replaces = [a + c + b[1:] for a, b in splits for c in letters if b]
        inserts = [a + c + b for a, b in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)


    def _edits2(self, word):
        """
        Generate all possible edits at a distance of 2 from the given word.

        Parameters:
            word (str): The word for which edits are generated.

        Returns:
            set: Set of possible edits.
        """
        return (e2 for e1 in self._edits1(word) for e2 in self._edits1(e1))