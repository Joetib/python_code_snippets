# Let's create a file size calculator in Python
import os

file_path = input("Enter file path: ")
# Check if file exists
if os.path.exists(file_path):
    # Get file size in bytes
    file_size = os.path.getsize(file_path)
    # Convert bytes to KB, MB, GB
    kb_size = file_size / 1024
    mb_size = kb_size / 1024
    gb_size = mb_size / 1024
    # Output file size in different units
    print(f"File size: {file_size} bytes")
    print(f"File size: {kb_size:.2f} KB")
    print(f"File size: {mb_size:.2f} MB")
    print(f"File size: {gb_size:.2f} GB")
else:
    print("File not found.")
# Output
# >> File size: 1024 bytes
# >> File size: 1.00 KB
# >> File size: 0.00 MB
# >> File size: 0.00 GB
# Please Like and Subscribe