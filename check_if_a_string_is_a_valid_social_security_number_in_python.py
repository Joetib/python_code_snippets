# We can use regular expressions to check if a string is a valid social security number in Python.
# We'll use the `re` module which is a built-in module in Python.

import re

def is_valid_ssn(ssn):
    # Define the pattern for a valid social security number
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    
    # Use the `re.match()` function to check if the string matches the pattern
    if re.match(pattern, ssn):
        return True
    else:
        return False

# Test the function with some examples
print(is_valid_ssn("123-45-6789"))  # True
print(is_valid_ssn("123-456-789"))  # False
print(is_valid_ssn("123456789"))    # False
# Please Like and Subscribe