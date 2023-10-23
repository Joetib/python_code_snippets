# To remove all occurrences of a character from a list in Python,
# you can use a list comprehension to filter out the character.

# Example list
my_list = ['a', 'b', 'c', 'a', 'd', 'e', 'a']

# Character to remove
char_to_remove = 'a'

# Remove all occurrences of the character from the list
my_list = [x for x in my_list if x != char_to_remove]

# Output the updated list
print(my_list)

# Output
# >> ['b', 'c', 'd', 'e']
# Please Like and Subscribe