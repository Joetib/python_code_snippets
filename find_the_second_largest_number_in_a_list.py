# We can find the second largest number in a list by sorting the list in descending order and then accessing the element at index 1.

numbers = [5, 10, 3, 8, 2, 7]
second_largest = sorted(numbers, reverse=True)[1]
print(second_largest)

# Output
# 8
# Please Like and Subscribe