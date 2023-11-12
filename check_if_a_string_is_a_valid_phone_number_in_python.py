# We can use regular expressions to check if a string is a valid phone number.
# We'll use the `re` module in Python for this task.

import re

def is_valid_phone_number(phone_number):
    # Define the regular expression pattern for a valid phone number
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    
    # Use the `re.match()` function to check if the phone number matches the pattern
    if re.match(pattern, phone_number):
        return True
    else:
        return False

# Test the function with a phone number
phone_number = input("Enter a phone number: ")
print(is_valid_phone_number(phone_number))

# Output
# >> Enter a phone number: 123-456-7890
# >> True
# Please Like and Subscribe