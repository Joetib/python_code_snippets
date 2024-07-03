# Let's create a text file splitter based on line count
input_file = 'input.txt'
output_prefix = 'output'
lines_per_file = 100

with open(input_file) as f:
    current_file = None
    line_count = 0
    for line in f:
        if line_count % lines_per_file == 0:
            if current_file:
                current_file.close()
            current_file = open(f'{output_prefix}_{line_count // lines_per_file}.txt', 'w')
        current_file.write(line)
        line_count += 1
    if current_file:
        current_file.close()

# This code reads an input file and splits it into multiple
# output files based on the specified number of lines per file
# Please Like and Subscribe