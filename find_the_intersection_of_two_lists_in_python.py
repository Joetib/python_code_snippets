# We can use the built-in set data structure in Python to find the intersection of two lists.
# Here's how we can do it:

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Convert the lists to sets
set1 = set(list1)
set2 = set(list2)

# Find the intersection of the sets
intersection = set1.intersection(set2)

# Convert the intersection set back to a list
intersection_list = list(intersection)

# Print the intersection list
print(intersection_list)

# Output
# >> [4, 5]
# Please Like and Subscribe