# Let's create a file content replacer in Python
# No external libraries needed

file_path = "example.txt"
old_content = "old"
new_content = "new"

with open(file_path, 'r') as file:
    file_data = file.read()

file_data = file_data.replace(old_content, new_content)

with open(file_path, 'w') as file:
    file.write(file_data)

# This code reads a file, replaces old content with new content,
# and writes the updated content back to the file
# Please Like and Subscribe