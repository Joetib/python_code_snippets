# We can use the `set` data structure to find the common elements between two lists.
# First, we convert both lists to sets using the `set()` function.
# Then, we use the `intersection()` method to find the common elements between the two sets.
# Finally, we convert the result back to a list using the `list()` function.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = list(set(list1).intersection(set(list2)))

print(common_elements)

# Output:
# [4, 5]
# Please Like and Subscribe