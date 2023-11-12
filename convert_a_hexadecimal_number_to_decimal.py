# We can use the built-in `int()` function in Python to convert a hexadecimal number to decimal.
# The `int()` function takes two arguments: the hexadecimal number as a string and the base, which is 16 for hexadecimal.
# The function returns the decimal representation of the hexadecimal number.

hex_number = input("Enter a hexadecimal number: ")
decimal_number = int(hex_number, 16)
print(decimal_number)

# Example:
# Enter a hexadecimal number: 1A
# Output: 26
# Please Like and Subscribe