# Let's create a simple text file searcher in Python
import os

# Define the directory to search
directory = 'path/to/directory'

# Define the keyword to search for
keyword = 'your_keyword'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename), 'r') as file:
            # Read the file line by line
            for line in file:
                # Check if the keyword is in the line
                if keyword in line:
                    print(f'Found in {filename}: {line}')

# Output
# >> Found in example.txt: This is a line with your_keyword
# Please Like and Subscribe