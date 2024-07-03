# Let's create a file content sorter in Python
# First, read the content of a file
with open('file.txt', 'r') as file:
    content = file.readlines()
# Sort the content alphabetically
sorted_content = sorted(content)
# Write the sorted content to a new file
with open('sorted_file.txt', 'w') as sorted_file:
    sorted_file.writelines(sorted_content)
# Output
# The content of 'file.txt' will be sorted alphabetically
# Please Like and Subscribe