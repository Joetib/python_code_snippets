# We can use the `os` module in Python to find files in a directory.
# Here's a simple implementation of a file finder:

import os

def find_files(directory, extension):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_paths.append(os.path.join(root, file))
    return file_paths

# Example usage:
directory = input("Enter directory: ")
extension = input("Enter file extension: ")

files = find_files(directory, extension)
print(files)
# Output:
# ['/path/to/file1.txt', '/path/to/file2.txt', ...]
# Please Like and Subscribe