# CreoleNLTK: Creole Natural Language Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

CreoleNLTK is a Python library designed for preprocessing Creole text. The library includes various functions and tools to prepare text data for natural language processing (NLP) tasks. It provides functionality for cleaning, tokenization, lowercasing, stopword removal, contraction to expansion, and spelling checking.

## Features

- **Text Cleaning:** Remove unwanted characters and clean the text.
- **Tokenization:** Break the text into words or tokens.
- **Lowercasing:** Convert text to lowercase.
- **Stopword Removal:** Remove common words that do not contribute much to the meaning.
- **Contraction to Expansion:** Expand contractions in the text.
- **Spelling Check:** Identify and correct spelling errors.

## Installation

You can install CreoleNLTK using pip:

```bash
pip install creolenltk
```

## Usage

````python
from creole_preprocessor import clean_text, tokenize_text, lowercase_text, remove_stopwords, expand_contractions, spell_check

### Example Usage
text = "Some Creole text with contractions, special characters, and misspellings."

### Clean text
cleaned_text = clean_text(text)

### Tokenization
tokens = tokenize_text(cleaned_text)

### Lowercasing
lowercased_text = lowercase_text(cleaned_text)

### Stopword Removal
text_without_stopwords = remove_stopwords(cleaned_text)

### Contraction to Expansion
expanded_text = expand_contractions(cleaned_text)

### Spelling Check
corrected_text = spell_check(cleaned_text)
````
For more detailed usage and examples, refer to the documentation.

## License

MIT licensed. See the bundled [LICENSE](LICENSE) file for more details.

