# To count the number of words in a string, we can split the string into a list of words using the `split()` method, and then count the number of elements in the list using the `len()` function.

string = input("Enter a string: ")
# Split the string into a list of words
words = string.split()
# Count the number of words
word_count = len(words)
print("Number of words:", word_count)

# Example input: "Hello world, how are you?"
# Output: Number of words: 5
# Please Like and Subscribe