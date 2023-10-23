# To convert a decimal number to binary, we can use the built-in `bin()` function in Python.
# The `bin()` function takes an integer as input and returns its binary representation as a string.

decimal_number = int(input("Enter a decimal number: "))
binary_number = bin(decimal_number)[2:]  # [2:] is used to remove the '0b' prefix from the binary string

print(binary_number)

# Example:
# Input: 10
# Output: 1010
# Please Like and Subscribe