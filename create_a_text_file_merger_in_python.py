# Let's create a text file merger in Python
# No external libraries needed

# List of text files to merge
file_names = ['file1.txt', 'file2.txt', 'file3.txt']

# Open a new file to write the merged content
with open('merged_file.txt', 'w') as merged_file:
    for file_name in file_names:
        with open(file_name, 'r') as file:
            merged_file.write(file.read() + '\n')

# Merged_file.txt now contains the content of all files
# Please Like and Subscribe