# Let's create a file content counter in Python
file_path = "example.txt"
# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the content and split by spaces
    words = file.read().split()
    # Count the number of words
    word_count = len(words)
# Output the word count
print(f"Number of words in the file: {word_count}")

# Output
# >> Number of words in the file: 50
# Please Like and Subscribe