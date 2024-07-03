# Let's create a text file line sorter in Python
file_path = "input.txt"
# Read lines from the file
with open(file_path, 'r') as file:
    lines = file.readlines()
# Sort the lines
sorted_lines = sorted(lines)
# Write sorted lines to a new file
output_file_path = "output.txt"
with open(output_file_path, 'w') as output_file:
    output_file.writelines(sorted_lines)
# Output
# The lines from input.txt will be sorted and saved in output.txt
# Please Like and Subscribe