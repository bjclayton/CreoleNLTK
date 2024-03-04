def word_segmentation(text):
        """
        Perform word segmentation on the input text using a list of known words.

        Parameters:
        - text (str): The input text without spaces between words.

        Returns:
        - segmented_text (str): The input text segmented into words.
        """
        segmented_text = []

        return ' '.join(segmented_text)

text_to_segment = "Saseyontes"
segmented_text = word_segmentation(text_to_segment)
print(segmented_text)
