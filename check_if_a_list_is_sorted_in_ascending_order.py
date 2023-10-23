# To check if a list is sorted in ascending order, we can compare each element with its next element in the list.
# If any element is greater than its next element, then the list is not sorted in ascending order.

def is_sorted_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# Example usage:
lst = [1, 2, 3, 4, 5]
print(is_sorted_ascending(lst))
# Output: True

lst = [5, 4, 3, 2, 1]
print(is_sorted_ascending(lst))
# Output: False

lst = [1, 3, 2, 4, 5]
print(is_sorted_ascending(lst))
# Output: False
# Please Like and Subscribe