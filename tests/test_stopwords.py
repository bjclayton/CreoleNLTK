import unittest
from creolenltk.stopwords import Stopword  

class TestStopword(unittest.TestCase):

    def setUp(self):
        # Create an instance of the Stopword class for testing
        self.stopword_instance = Stopword()

    def test_load_stopwords(self):
        # Test if stopwords are loaded properly
        self.assertIsInstance(self.stopword_instance.stopwords, set)
        self.assertGreater(len(self.stopword_instance.stopwords), 0)

    def test_remove_stopwords(self):
        # Test the remove_stopwords method
        input_text = "Sa se yon fraz tès ak kèk stopwords komen nan Kreyòl Ayisyen."
        result_text = self.stopword_instance.remove_stopwords(input_text)
        expected_result = "fraz tès stopwords komen Kreyòl Ayisyen."
        self.assertEqual(result_text, expected_result)

    def test_is_stopword(self):
        # Test the is_stopword method
        stopword = "Sa"
        non_stopword = "Tomat"
        self.assertTrue(self.stopword_instance.is_stopword(stopword))
        self.assertFalse(self.stopword_instance.is_stopword(non_stopword))

if __name__ == '__main__':
    unittest.main()