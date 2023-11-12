# We can use the built-in bin() function to convert each integer
# in the list to its binary representation

# Example list of integers
integers = [10, 20, 30, 40, 50]

# Convert each integer to binary using list comprehension
binary_list = [bin(num) for num in integers]

# Output the binary list
print(binary_list)

# Output:
# ['0b1010', '0b10100', '0b11110', '0b101000', '0b110010']
# Please Like and Subscribe