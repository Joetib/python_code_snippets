# We can use the `re` module to convert a string to snake case in Python.
# The `re` module provides support for regular expressions.

import re

def to_snake_case(string):
    # Use regular expression to replace all non-alphanumeric characters with underscores
    snake_case_string = re.sub(r'\W+', '_', string).lower()
    return snake_case_string

# Example usage
text = input("Enter a string: ")
snake_case_text = to_snake_case(text)
print(snake_case_text)

# Output
# >> Enter a string: Convert a String to Snake Case
# >> convert_a_string_to_snake_case
# Please Like and Subscribe