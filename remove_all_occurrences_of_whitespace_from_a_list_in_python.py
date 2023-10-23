# We can use list comprehension to remove all occurrences of whitespace from a list
# Let's define a list with whitespace
my_list = ['hello', 'world', ' ', 'python', ' ', 'programming']

# Use list comprehension to remove whitespace
my_list = [item for item in my_list if item.strip()]

# Print the updated list
print(my_list)
# Please Like and Subscribe