# Let's create a simple Python script to count the number
# of lines in a file

file_path = "example.txt"
# Open the file in read mode
with open(file_path, 'r') as file:
    # Count the number of lines
    line_count = sum(1 for line in file)
    
# Output the line count
print("Number of lines:", line_count)
# Please Like and Subscribe