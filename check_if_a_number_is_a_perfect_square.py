# To check if a number is a perfect square, we can use the math module in Python.
# The math module provides a function called sqrt() which returns the square root of a number.
# If the square root of a number is an integer, then the number is a perfect square.

import math

def is_perfect_square(num):
    # Calculate the square root of the number
    sqrt = math.sqrt(num)
    
    # Check if the square root is an integer
    if sqrt.is_integer():
        return True
    else:
        return False

# Test the function
num = int(input("Enter a number: "))
print(is_perfect_square(num))

# Example Output:
# Enter a number: 16
# True
# Please Like and Subscribe