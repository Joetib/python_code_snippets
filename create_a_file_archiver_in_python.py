# Let's create a simple file archiver using zipfile module
import zipfile

# List of files to be archived
files = ['file1.txt', 'file2.txt']

# Name of the archive file
archive_name = 'my_archive.zip'

# Create a new zip file
with zipfile.ZipFile(archive_name, 'w') as zipf:
    # Add each file in the list to the archive
    for file in files:
        zipf.write(file)

# Output
# A zip file named 'my_archive.zip' containing 'file1.txt' and 'file2.txt'
# Please Like and Subscribe