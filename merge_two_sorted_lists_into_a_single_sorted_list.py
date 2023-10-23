# We can use the `merge` function from the `heapq` module to merge two sorted lists into a single sorted list.
# The `merge` function takes two or more sorted iterables and returns an iterator that produces the sorted values from all the inputs.

# Let's say we have two sorted lists `list1` and `list2`.
# We can merge them into a single sorted list `merged_list` using the `merge` function.

import heapq

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

merged_list = list(heapq.merge(list1, list2))

print(merged_list)

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8]
# Please Like and Subscribe