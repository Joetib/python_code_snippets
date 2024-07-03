# Let's create a function to remove content from a file
def remove_content(file_path):
    with open(file_path, 'w') as file:
        file.truncate(0)
# Usage: provide the file path to remove content
# remove_content("example.txt")
# Please Like and Subscribe