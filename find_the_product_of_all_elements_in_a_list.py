# To find the product of all elements in a list, we can use the `reduce` function from the `functools` module.

from functools import reduce

# Define a list of numbers
numbers = [2, 3, 4, 5]

# Use the `reduce` function with a lambda function to multiply all elements
product = reduce(lambda x, y: x * y, numbers)

# Output the product
print(product)

# Output:
# 120
# Please Like and Subscribe