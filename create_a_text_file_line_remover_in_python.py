# Let's create a function to remove specific lines from a text file
file_path = "example.txt"
lines_to_remove = [2, 4]  # Specify line numbers to remove

def remove_lines(file_path, lines_to_remove):
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for index, line in enumerate(lines, start=1):
            if index not in lines_to_remove:
                file.write(line)

# Let's call the function to remove specified lines
remove_lines(file_path, lines_to_remove)
# Please Like and Subscribe