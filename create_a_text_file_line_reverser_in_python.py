# Let's create a function that reads a text file, reverses
# the order of lines, and writes the result to a new file

def reverse_lines(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    with open(output_file, 'w') as file:
        file.writelines(reversed(lines))

# Example usage
reverse_lines("input.txt", "output.txt")
# This will reverse the lines in input.txt and save to output.txt
# Please Like and Subscribe