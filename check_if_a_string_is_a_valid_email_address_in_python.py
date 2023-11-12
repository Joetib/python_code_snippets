# We can use the `re` module in Python to check if a string is a valid email address.
# The regular expression pattern for validating an email address is quite complex,
# so we'll use a simplified version that covers most common cases.

import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Let's test the function with some examples
print(is_valid_email("john.doe@example.com"))  # True
print(is_valid_email("jane.doe@example"))     # False
print(is_valid_email("invalid.email@com"))     # False


# Please Like and Subscribe