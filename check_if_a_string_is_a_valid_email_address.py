# We can use regular expressions to check if a string is a valid email address.
# The regular expression pattern for validating email addresses is:
# ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# Test the function
email = input("Enter an email address: ")
print(is_valid_email(email))

# Example usage:
# Enter an email address: test@example.com
# True
# Please Like and Subscribe