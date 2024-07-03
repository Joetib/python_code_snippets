# Let's create a script to find duplicate files in a directory
# >> pip install hashlib
import os
import hashlib
def find_duplicates(directory):
    duplicates = {}
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            with open(filepath, 'rb') as file:
                file_hash = hashlib.md5(file.read()).hexdigest()
            if file_hash in duplicates:
                duplicates[file_hash].append(filepath)
            else:
                duplicates[file_hash] = [filepath]
    return {k: v for k, v in duplicates.items() if len(v) > 1}
directory = input("Enter directory path: ")
duplicate_files = find_duplicates(directory)
for file_hash, files in duplicate_files.items():
    print(f"Duplicate files with hash {file_hash}:")
    for file in files:
        print(file)
# Please Like and Subscribe