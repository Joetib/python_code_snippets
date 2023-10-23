# To check if a list contains only unique elements, we can convert the list to a set and compare the lengths of the list and the set.
# If the lengths are equal, it means all elements in the list are unique.

my_list = [1, 2, 3, 4, 5]
is_unique = len(my_list) == len(set(my_list))
print(is_unique)

# Output
# >> True
# Please Like and Subscribe