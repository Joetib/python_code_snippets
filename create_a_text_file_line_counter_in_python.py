# Let's create a Python script to count the number of lines
# in a text file

file_path = "sample.txt"  # specify the path to the text file

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

# Count the number of lines
num_lines = len(lines)

# Output the number of lines
print(f"Number of lines in the file: {num_lines}")

# Output
# >> Number of lines in the file: 10
# Please Like and Subscribe