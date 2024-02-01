import unittest
from creolenltk import ContractionToExpansion


class TestContractionToExpansion(unittest.TestCase):

    def setUp(self):
        # Create an instance of the ContractionToExpansion class for testing
        self.contraction_expander = ContractionToExpansion()

    def test_expand_contractions(self):
        # Test the expand_contractions method
        # Test with a sentence containing contractions
        input_text = "mw pa ka ale jodia, m'ap rete lakay."
        result_text = self.contraction_expander.expand_contractions(input_text)
        expected_result = "mwen pa kapab ale jodia, mwen ap rete lakay."
        self.assertEqual(result_text, expected_result)

        input_text_no_contractions = "L di l'ap manje manje a midi poutan l pa manje vre."
        expected_result = "li di li ap manje manje a midi poutan li pa manje vre."
        result_text_no_contractions = self.contraction_expander.expand_contractions(input_text_no_contractions)
        self.assertEqual(result_text_no_contractions, expected_result)

        # Test with an empty string
        input_empty_string = ""
        result_empty_string = self.contraction_expander.expand_contractions(input_empty_string)
        self.assertEqual(result_empty_string, input_empty_string)

        # Test with None input
        input_none = None
        result_none = self.contraction_expander.expand_contractions(input_none)
        self.assertEqual(result_none, input_none)


if __name__ == '__main__':
    unittest.main()
