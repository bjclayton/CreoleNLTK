import unittest
from creolenltk.spelling_checker import SpellingChecker


class TestSpellingChecker(unittest.TestCase):
    def setUp(self):
        self.spelling = SpellingChecker()

    def test_correction(self):
        assert self.spelling.correction('òtgraf') == 'òtograf'
        assert self.spelling.correction('korrijje') == 'korije'
        assert self.spelling.correction('potoa') == 'poto'
        assert self.spelling.correction('aranje') == 'ranje'
        assert self.spelling.correction('manifesstee') == 'manifeste'
        assert self.spelling.correction('manqh') == 'manch'
        assert self.spelling.correction('privo') == 'prive'
        assert self.spelling.correction('mo') == 'mo'
        assert self.spelling.correction('ekselan') == 'ekselan'


if __name__ == '__main__':
    unittest.main()
