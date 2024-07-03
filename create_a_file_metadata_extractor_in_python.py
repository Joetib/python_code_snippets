# Use the exifread library to extract metadata from image files
# Install exifread using
# >> pip install exifread

import exifread

def extract_metadata(file_path):
    with open(file_path, 'rb') as file:
        tags = exifread.process_file(file)
        for tag in tags.keys():
            print(f"{tag}: {tags[tag]}")

# Provide the file path to extract metadata
file_path = "example.jpg"
extract_metadata(file_path)
# Please Like and Subscribe