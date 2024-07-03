# To create a file organizer in Python, we can use the `os` module to interact with the file system.
# We will organize files in a specified directory based on their file extensions.
import os
import shutil
directory = '/path/to/directory'

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            
            if not os.path.exists(os.path.join(directory, file_extension)):
                os.makedirs(os.path.join(directory, file_extension))
            # Move the file to the corresponding directory
            shutil.move(file_path, os.path.join(directory, file_extension, filename))

# Call the function to organize files in the specified directory
organize_files(directory)

# Output:
# The files in the directory will be organized into separate directories based on their file extensions.
# Please Like and Subscribe