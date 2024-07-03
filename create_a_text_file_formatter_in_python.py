# Let's create a text file formatter that reads a text file,
# removes extra spaces, and writes the formatted text to a new file

input_file = 'input.txt'
output_file = 'output.txt'

# Read input file and format text
with open(input_file, 'r') as file:
    lines = file.readlines()
    formatted_text = ' '.join([line.strip() for line in lines])

# Write formatted text to output file
with open(output_file, 'w') as file:
    file.write(formatted_text)

# The input.txt file should contain the text to be formatted
# The output will be written to output.txt
# Example input.txt: "  Hello    World!  "
# Example output.txt: "Hello World!"
# Please Like and Subscribe