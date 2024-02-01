import unittest
from creolenltk import Tokenizer


class TestTokenizer(unittest.TestCase):

    def setUp(self):
        # Create an instance of the Tokenizer class for testing
        self.tokenizer = Tokenizer()

    def test_word_tokenize(self):
        # Test the word_tokenize method
        # Test with a simple sentence
        input_text = "Sa se yon fraz senp"
        result_tokens = self.tokenizer.word_tokenize(input_text)
        expected_tokens = ["sa", "se", "yon", "fraz", "senp"]
        self.assertEqual(result_tokens, expected_tokens)

        # Test with a sentence containing contractions
        input_text_with_contractions = "mw paka kwè sa rive."
        result_tokens_with_contractions = self.tokenizer.word_tokenize(input_text_with_contractions,
                                                                       expand_contractions=True)
        expected_tokens_with_contractions = ["mwen", "pa", "kapab", "kwè", "sa", "rive"]
        self.assertEqual(result_tokens_with_contractions, expected_tokens_with_contractions)

        # Test with an empty string
        input_empty_string = ""
        result_empty_string = self.tokenizer.word_tokenize(input_empty_string)
        self.assertEqual(result_empty_string, [])

        # Test with None input
        input_none = None
        result_none = self.tokenizer.word_tokenize(input_none)
        self.assertEqual(result_none, [])


if __name__ == '__main__':
    unittest.main()
