# We can use the `shutil` module in Python to merge multiple files into one.

# First, we need to import the `shutil` module
import shutil

# Define a function to merge files
def merge_files(output_file, *input_files):
    with open(output_file, 'wb') as outfile:
        for file in input_files:
            with open(file, 'rb') as infile:
                shutil.copyfileobj(infile, outfile)

# Usage example:
# merge_files('merged_file.txt', 'file1.txt', 'file2.txt', 'file3.txt')

# This will merge the contents of 'file1.txt', 'file2.txt', and 'file3.txt'
# into a new file called 'merged_file.txt'
# Please Like and Subscribe