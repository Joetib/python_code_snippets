# Let's create a text file splitter in Python
# This code will read a text file and split it into
# smaller files based on the number of lines
# No external libraries needed

def split_text_file(input_file, lines_per_file):
    with open(input_file, 'r') as file:
        data = file.readlines()
    
    for i in range(0, len(data), lines_per_file):
        with open(f'{input_file}_{i//lines_per_file}.txt', 'w') as file:
            file.writelines(data[i:i+lines_per_file])

# Let's split a text file 'input.txt' into files with 10 lines each
split_text_file('input.txt', 10)
# This will create files like 'input.txt_0.txt', 'input.txt_1.txt', etc.
# Please Like and Subscribe