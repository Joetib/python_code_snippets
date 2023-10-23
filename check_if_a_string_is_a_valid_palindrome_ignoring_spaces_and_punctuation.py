# We can check if a string is a valid palindrome by removing all spaces and punctuation from the string and comparing it with its reverse. If they are the same, then the string is a valid palindrome.

import re

def is_valid_palindrome(string):
    # Remove spaces and punctuation from the string
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', string)
    
    # Compare the cleaned string with its reverse
    return cleaned_string.lower() == cleaned_string.lower()[::-1]

# Test the function
string = input("Enter a string: ")
print(is_valid_palindrome(string))

# Example:
# Input: "A man, a plan, a canal: Panama"
# Output: True
# Please Like and Subscribe