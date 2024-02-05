import unittest
from creolenltk import SpellingChecker


class TestSpellingChecker(unittest.TestCase):
    def setUp(self):
        self.spelling = SpellingChecker()

    def test_correct_word(self):
        self.assertEqual(self.spelling.correct_word('òtgraf'), 'òtograf')
        self.assertEqual(self.spelling.correct_word('korrijje'), 'korije')
        self.assertEqual(self.spelling.correct_word('potoa'), 'poto')
        self.assertEqual(self.spelling.correct_word('aranje'), 'ranje')
        self.assertEqual(self.spelling.correct_word('manifesstee'), 'manifeste')
        self.assertEqual(self.spelling.correct_word('manqh'), 'manch')
        self.assertEqual(self.spelling.correct_word('privo'), 'prive')
        self.assertEqual(self.spelling.correct_word('mo'), 'mo')
        self.assertEqual(self.spelling.correct_word('ekselan'), 'ekselan')

    def test_correct(self):
        input_text = "M prall fè yon tès soou fraz sa"
        expected_output = "mwen pral fè yon tès sou fraz sa"
        self.assertEqual(self.spelling.correct(input_text), expected_output)

        input_text = "èskke mwin ka genyan yon moso gaoto"
        expected_output = "èske mwen kapab genyen yon moso gato"
        self.assertEqual(self.spelling.correct(input_text), expected_output)


if __name__ == '__main__':
    unittest.main()
