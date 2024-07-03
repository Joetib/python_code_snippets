# Let's create a simple file comparison tool in Python
import filecmp

file1 = "file1.txt"
file2 = "file2.txt"

# Compare the two files
result = filecmp.cmp(file1, file2)

if result:
    print("Files are the same.")
else:
    print("Files are different.")

# Output
# >> Files are the same. (if files are identical)
# >> Files are different. (if files are not identical)
# Please Like and Subscribe