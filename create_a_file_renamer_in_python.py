import os

def rename_files(directory, prefix):
    """
    This function renames all files in a directory with a given prefix.
    :param directory: The directory path where the files are located.
    :param prefix: The prefix to be added to the file names.
    """
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            new_filename = prefix + filename
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# Example usage
directory = input("Enter directory path: ")
prefix = input("Enter prefix: ")
rename_files(directory, prefix)
# Please Like and Subscribe