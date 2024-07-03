# Let's create a simple text analyzer in Python.
# We will count the number of words, characters, and sentences in a given text.

text = input("Enter text: ")

# Counting the number of words
word_count = len(text.split())

# Counting the number of characters
char_count = len(text)

# Counting the number of sentences
sentence_count = text.count('.') + text.count('!') + text.count('?')

# Output the analysis
print("Word count:", word_count)
print("Character count:", char_count)
print("Sentence count:", sentence_count)
# Output
# Enter text: This is a sample text. It has multiple sentences!
# Word count: 8
# Character count: 47
# Sentence count: 2
# Please Like and Subscribe