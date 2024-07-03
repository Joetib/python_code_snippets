# Let's create a file line sorter in Python
# Read lines from a file, sort them, and write to a new file

# Read lines from input file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Sort the lines
lines.sort()

# Write sorted lines to output file
with open('output.txt', 'w') as file:
    file.writelines(lines)
# Please Like and Subscribe