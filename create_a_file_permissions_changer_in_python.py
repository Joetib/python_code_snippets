# Let's create a Python script to change file permissions
import os

# Specify the file path
file_path = "example.txt"

# Define the new permissions (e.g., 0o777 for full permissions)
new_permissions = 0o777

# Change the file permissions
os.chmod(file_path, new_permissions)

# Output
# The permissions of 'example.txt' have been changed.
# Please Like and Subscribe