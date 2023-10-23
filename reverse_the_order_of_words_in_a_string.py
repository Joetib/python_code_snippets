# To reverse the order of words in a string, we can follow these steps:
# 1. Split the string into a list of words using the split() method.
# 2. Reverse the order of the words in the list using the reverse() method.
# 3. Join the reversed words back into a string using the join() method.

# Let's see the implementation:

string = input("Enter a string: ")
# Split the string into a list of words
words = string.split()
# Reverse the order of the words
words.reverse()
# Join the reversed words back into a string
reversed_string = ' '.join(words)

print(reversed_string)

# Example Input: "Hello World"
# Output: "World Hello"
# Please Like and Subscribe