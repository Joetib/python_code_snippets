# To convert a binary number to decimal, we can use the built-in `int` function in Python.
# The `int` function can convert a string representation of a number to its corresponding integer value.
# We can pass the binary number as a string to the `int` function and specify the base as 2.

binary_number = input("Enter a binary number: ")
decimal_number = int(binary_number, 2)

print(decimal_number)

# Example Input
# Enter a binary number: 1010
# Output
# 10
# Please Like and Subscribe