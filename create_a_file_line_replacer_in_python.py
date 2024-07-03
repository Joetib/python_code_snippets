# Let's create a Python script to replace a specific line in a file

file_path = "example.txt"
line_number = 3
new_line = "This is the new line content"

with open(file_path, 'r') as file:
    lines = file.readlines()

lines[line_number - 1] = new_line + '\n'

with open(file_path, 'w') as file:
    file.writelines(lines)

# This script replaces line number 3 in 'example.txt' with
# 'This is the new line content'
# Please Like and Subscribe