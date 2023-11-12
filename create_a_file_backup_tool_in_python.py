# Let's create a file backup tool in Python
# We'll use the shutil module to copy files
# No additional packages need to be installed

import shutil

def backup_file(source_file, destination_folder):
    """
    Function to backup a file to a specified destination folder.
    :param source_file: The path of the file to be backed up.
    :param destination_folder: The path of the folder where the backup will be stored.
    """
    try:
        shutil.copy2(source_file, destination_folder)
        print("File backup successful!")
    except FileNotFoundError:
        print("Source file not found.")
    except IsADirectoryError:
        print("Destination folder is not valid.")
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage
source_file = input("Enter the path of the file to be backed up: ")
destination_folder = input("Enter the path of the destination folder: ")
backup_file(source_file, destination_folder)
# Please Like and Subscribe