# Let's create a file splitter that splits a file based on line count
# No external libraries needed

def split_file(input_file, lines_per_file):
    with open(input_file) as f:
        all_lines = f.readlines()
    
    for i in range(0, len(all_lines), lines_per_file):
        with open(f'{input_file}_part_{i//lines_per_file + 1}.txt', 'w') as f:
            f.writelines(all_lines[i:i+lines_per_file])

# Usage
split_file('input.txt', 10)
# This will split 'input.txt' into multiple files with 10 lines each
# Please Like and Subscribe