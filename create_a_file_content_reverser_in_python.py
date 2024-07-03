# Let's create a file content reverser in Python
file_path = "example.txt"
with open(file_path, 'r') as file:
    content = file.read()
reversed_content = content[::-1]
with open(file_path, 'w') as file:
    file.write(reversed_content)
# This will reverse the content of the file "example.txt"
# Please Like and Subscribe