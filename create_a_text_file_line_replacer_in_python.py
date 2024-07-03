# Let's create a Python script to replace a specific line
# in a text file
# No external packages needed

file_path = 'sample.txt'
line_number = 3
new_line = 'This is the new line'

with open(file_path, 'r') as file:
    lines = file.readlines()

lines[line_number - 1] = new_line + '\n'

with open(file_path, 'w') as file:
    file.writelines(lines)

# This script will replace line 3 in 'sample.txt' with
# 'This is the new line'
# Please Like and Subscribe