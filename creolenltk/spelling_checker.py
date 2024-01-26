import re
from collections import Counter
import string

class SpellingChecker:
    """
    A class for correcting spelling errors in text based on: Peter Norvig, "How to Write a Spelling Corrector", http://norvig.com/spell-correct.html

    Methods:
        - suggest(word): Corrects spelling errors in the word.
    """

    def __init__(self):
        """
        Initialize the spelling checker with a words.
        """
        self._WORDS = self._load()


    def _load(self):
        with open('data\\creole_words.txt', encoding='utf-8') as file:
            words = file.read()
        return Counter(self._extract_words(words))


    def _extract_words(self, text):
        """
        Extract words from the given text.
        """
        return re.findall(r'\w+', text.lower())


    def _probability(self, word):
        """
        Return the probability of the given word.
        """
        total_words = sum(self._WORDS.values())
        return self._WORDS[word] / total_words
    

    def suggests(self, word):
        """
        Return the most probable correction for the given word.
        """
        return max(self._candidates(word), key=self._probability)


    def _candidates(self, word):
        """
        Generate possible spelling corrections for the given word.
        """
        if len(word) == 1:
            return word
        if word in string.punctuation:
            return word
        if word in string.whitespace:
            return word
        if word.replace(".", "").isdigit() or word.replace(",", "").isdigit():
            return word
        
        return (self._known([word]) or
                self._known(self._edits1(word)) or
                self._known(self._edits2(word)) or
                [word])
    

    def _known(self, words):
        """
        Filter the list of words to include only those present in the words list.
        """
        return set(w for w in words if w in self._WORDS)


    def _edits1(self, word):
        """
        Generate all possible edits at a distance of 1 from the given word.
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
        """
        return (e2 for e1 in self._edits1(word) for e2 in self._edits1(e1))