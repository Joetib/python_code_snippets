# Let's create a Python script to remove specific lines from a file

file_path = "example.txt"
lines_to_remove = [2, 5]  # Specify the line numbers to remove

with open(file_path, "r") as file:
    lines = file.readlines()

with open(file_path, "w") as file:
    for index, line in enumerate(lines, start=1):
        if index not in lines_to_remove:
            file.write(line)

# This script will remove lines 2 and 5 from the file
# Please Like and Subscribe