# We can use the `string` module to get a string of all punctuation characters
# Then we can use the `translate` method to remove all punctuation characters from a string

import string

def remove_punctuation(text):
    # Create a translation table with all punctuation characters mapped to None
    translation_table = str.maketrans("", "", string.punctuation)
    # Use the translation table to remove all punctuation characters from the text
    text_without_punctuation = text.translate(translation_table)
    return text_without_punctuation

# Example usage
text = "Hello, World!"
text_without_punctuation = remove_punctuation(text)
print(text_without_punctuation)
# Output
# >> Hello World
# Please Like and Subscribe