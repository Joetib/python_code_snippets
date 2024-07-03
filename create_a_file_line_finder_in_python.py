# Let's create a function that finds a specific line in a file
def find_line_in_file(file_path, target_line):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if target_line in line:
                return f"Line {line_number}: {line.strip()}"

# Example usage
file_path = 'example.txt'
target_line = 'specific text'
print(find_line_in_file(file_path, target_line))
# Output
# >> Line 5: This is the specific text we are looking for
# Please Like and Subscribe