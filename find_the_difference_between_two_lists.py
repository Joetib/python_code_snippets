# To find the difference between two lists, we can use the set data structure in Python.
# We can convert both lists to sets and then use the set difference operation to find the elements that are present in one list but not in the other.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Convert the lists to sets
set1 = set(list1)
set2 = set(list2)

# Find the difference between the sets
difference = set1 - set2

# Convert the difference set back to a list
result = list(difference)

print(result)

# Output:
# [1, 2, 3]
# Please Like and Subscribe