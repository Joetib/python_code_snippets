# Let's create a function that finds a specific line in a text file

def find_line_in_file(file_path, target_line):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if target_line in line:
                return f"Found '{target_line}' in line {line_number}"
    return f"'{target_line}' not found in the file"

# Example: Find 'hello' in 'example.txt'
result = find_line_in_file('example.txt', 'hello')
print(result)
# Output
# >> Found 'hello' in line 3
# Please Like and Subscribe