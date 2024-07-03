# Let's create a text file merger based on line count
# No need to install any external packages

file1 = 'file1.txt'
file2 = 'file2.txt'
output_file = 'merged_file.txt'

with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
    # Read lines from file1 and write to output file
    for line in f1:
        out.write(line)
    
    # Read lines from file2 and write to output file
    for line in f2:
        out.write(line)

# Merged file created with lines from both file1 and file2
# Please Like and Subscribe