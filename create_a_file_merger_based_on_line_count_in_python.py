# Let's create a file merger based on line count
# This script merges files if the total line count is below a threshold

import os

# Set the threshold line count
threshold = 100

# List all files in the current directory
files = [f for f in os.listdir() if os.path.isfile(f)]

# Initialize merged content
merged_content = ""

# Loop through each file
for file in files:
    with open(file, 'r') as f:
        # Read lines from the file
        lines = f.readlines()
        # Check if adding the lines exceeds the threshold
        if len(merged_content.split('\n')) + len(lines) <= threshold:
            merged_content += ''.join(lines)

# Write the merged content to a new file
with open('merged_file.txt', 'w') as f:
    f.write(merged_content)

# Output
# A new file 'merged_file.txt' will be created with merged content
# Please Like and Subscribe