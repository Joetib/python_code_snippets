def is_palindrome(s):
    # Base case: if the string is empty or has only one character, it is a palindrome
    if len(s) <= 1:
        return True
    # Recursive case: check if the first and last characters are equal
    if s[0] == s[-1]:
        # Recursively check if the substring without the first and last characters is a palindrome
        return is_palindrome(s[1:-1])
    else:
        return False

# Test the function
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# Please Like and Subscribe