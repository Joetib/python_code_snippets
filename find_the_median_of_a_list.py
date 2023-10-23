# To find the median of a list, we can follow these steps:
# 1. Sort the list in ascending order.
# 2. If the length of the list is odd, return the middle element.
# 3. If the length of the list is even, return the average of the two middle elements.

# Let's implement this in code:

def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2

# Example usage:
numbers = [5, 2, 9, 1, 7]
median = find_median(numbers)
print(median)

# Output:
# 5.0
# Please Like and Subscribe