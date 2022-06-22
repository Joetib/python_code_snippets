# In todays video we will learn how to read data from file

# to open a file we use the open builtin function
file = open(file="file_name.txt") 
# replace 'file_name.txt' with the name of your file

# To read the content we use the read method
content = file.read()

# Always close the file after reading from it.
file.close()

print(content)

# Please Like and Subscribe