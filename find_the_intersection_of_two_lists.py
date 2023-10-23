# We can use the built-in set data structure in Python to find the intersection of two lists.
# First, we convert both lists into sets using the set() function.
# Then, we use the intersection operator '&' to find the common elements between the two sets.
# Finally, we convert the result back into a list using the list() function.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection = list(set(list1) & set(list2))

print(intersection)

# Output:
# [4, 5]
# Please Like and Subscribe