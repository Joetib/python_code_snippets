# To check if a string is a palindrome, we can compare the string with its reverse.
# If the string is equal to its reverse, then it is a palindrome.

def is_palindrome(string):
    return string == string[::-1]

# Testing the function
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
# Please Like and Subscribe