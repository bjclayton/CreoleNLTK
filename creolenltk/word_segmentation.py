def word_segmentation(text, word_list):
        """
        Perform word segmentation on the input text using a list of known words.

        Parameters:
        - text (str): The input text without spaces between words.
        - word_list (list): A list of known words for segmentation.

        Returns:
        - segmented_text (str): The input text segmented into words.
        """
        segmented_text = []

        # Implement your word segmentation logic here
        while text:
            for word in word_list:
                if text.startswith(word):
                    segmented_text.append(word)
                    text = text[len(word):]
                    break

        return ' '.join(segmented_text)

# Example usage
text_to_segment = "Thisisatestsentence"
known_words = ["This", "is", "a", "test", "sentence"]

segmented_text = word_segmentation(text_to_segment, known_words)
print(segmented_text)
