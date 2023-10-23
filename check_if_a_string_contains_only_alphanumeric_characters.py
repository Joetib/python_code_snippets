# We can use the `isalnum()` method of the string to check if a string contains only alphanumeric characters.
# The `isalnum()` method returns True if all characters in the string are alphanumeric (letters or numbers), and False otherwise.

string = input("Enter a string: ")
# Check if the string contains only alphanumeric characters
if string.isalnum():
    print("The string contains only alphanumeric characters")
else:
    print("The string does not contain only alphanumeric characters")

# Output:
# >> Enter a string: Hello123
# >> The string contains only alphanumeric characters
# Please Like and Subscribe