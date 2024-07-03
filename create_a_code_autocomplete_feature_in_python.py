# Use the Trie data structure for efficient autocomplete
# Install pytrie using
# >> pip install pytrie

from pytrie import StringTrie

# Initialize a Trie to store words for autocomplete
trie = StringTrie()

# Add words to the Trie for autocomplete
words = ["python", "java", "javascript", "ruby"]
for word in words:
    trie[word] = word

# Get autocomplete suggestions for a prefix
prefix = "py"
autocomplete = trie.values(prefix)
print(autocomplete)
# Output
# >> ['python']
# Please Like and Subscribe