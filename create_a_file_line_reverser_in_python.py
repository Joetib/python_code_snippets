# Let's create a Python script to reverse the lines in a file

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read the lines and store them in a list
    lines = file.readlines()

# Open the file in write mode
with open('output.txt', 'w') as file:
    # Write the lines in reverse order
    file.writelines(reversed(lines))

# This script will read lines from 'input.txt', reverse them,
# and write the reversed lines to 'output.txt'
# Please Like and Subscribe