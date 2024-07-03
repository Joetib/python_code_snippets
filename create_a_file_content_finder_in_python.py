# Let's create a file content finder in Python
import os

def find_in_files(directory, keyword):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):  # Search only in .txt files
                with open(os.path.join(root, file), 'r') as f:
                    if keyword in f.read():
                        print(f"Found '{keyword}' in {file}")

# Example usage
# find_in_files('/path/to/directory', 'search_keyword')
# Please Like and Subscribe