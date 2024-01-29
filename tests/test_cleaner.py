import unittest
from creolenltk.cleaner import Cleaner

class TestCleaner(unittest.TestCase):

    def setUp(self):
        # Create an instance of the Cleaner class for testing
        self.cleaner = Cleaner()

    def test_normalize_whitespace(self):
        input_text = "  Sa  a   se    yon  tès. "
        expected_output = "Sa a se yon tès."
        self.assertEqual(self.cleaner.normalize_whitespace(input_text), expected_output)
        

    def test_remove_html_tags(self):
        input_text = "<p>Sa se yon <b>tès</b>.</p>"
        expected_output = "Sa se yon tès."
        self.assertEqual(self.cleaner.remove_html_tags(input_text), expected_output)

    def test_remove_special_characters(self):
        input_text = "Sa se yon tès! Karaktè espesyal #$%@ retire."
        expected_output = "Sa se yon tès Karaktè espesyal retire"
        self.assertEqual(self.cleaner.remove_special_characters(input_text), expected_output)

    def test_remove_numbers(self):
        input_text = "Gen 123 pòm ak 456 zoranj."
        expected_output = "Gen pòm ak zoranj."
        self.assertEqual(self.cleaner.remove_numbers(input_text), expected_output)

    def test_clean_text(self):
        input_text = "<p>Sa se yon <b>tès</b>! Karaktè espesyal #$%@ retire. Gen 123 pòm.</p>"
        expected_output = "Sa se yon tès Karaktè espesyal retire Gen pòm"
        self.assertEqual(self.cleaner.clean_text(input_text, lowercase=False), expected_output)

if __name__ == '__main__':
    unittest.main()