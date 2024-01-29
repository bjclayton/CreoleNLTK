import unittest
from creolenltk.spelling_checker import SpellingChecker


class TestSpellingChecker(unittest.TestCase):
    def setUp(self):
        self.spelling = SpellingChecker()

    def test_correction(self):
        assert self.spelling.suggests('òtgraf') == 'òtograf'
        assert self.spelling.suggests('korrijje') == 'korije'
        assert self.spelling.suggests('potoa') == 'poto'
        assert self.spelling.suggests('aranje') == 'ranje'
        assert self.spelling.suggests('manifesstee') == 'manifeste'
        assert self.spelling.suggests('manqh') == 'manch'
        assert self.spelling.suggests('privo') == 'prive'
        assert self.spelling.suggests('mo') == 'mo'
        assert self.spelling.suggests('ekselan') == 'ekselan'


if __name__ == '__main__':
    unittest.main()
