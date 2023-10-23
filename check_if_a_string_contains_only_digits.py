# We can use the `isdigit()` method to check if a string contains only digits.
# The `isdigit()` method returns True if all characters in the string are digits, otherwise it returns False.

string = input("Enter a string: ")
# Check if the string contains only digits
if string.isdigit():
    print("The string contains only digits")
else:
    print("The string does not contain only digits")

# Output
# Enter a string: 12345
# The string contains only digits

# Enter a string: abc123
# The string does not contain only digits
# Please Like and Subscribe