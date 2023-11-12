# We can use a regular expression to check if a string is a valid hex color code in Python.
# We'll use the `re` module to perform the regular expression matching.

import re

def is_valid_hex_color(color):
    # The regular expression pattern to match a valid hex color code
    pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
    
    # Use the `re.match()` function to check if the color matches the pattern
    if re.match(pattern, color):
        return True
    else:
        return False

# Test the function with some examples
print(is_valid_hex_color("#123abc"))  # True
print(is_valid_hex_color("#FF00FF"))  # True
print(is_valid_hex_color("#123"))     # True
print(is_valid_hex_color("#GHIJKL"))  # False
print(is_valid_hex_color("123abc"))   # False
# Please Like and Subscribe