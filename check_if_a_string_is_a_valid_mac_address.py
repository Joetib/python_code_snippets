# We can use a regular expression to check if a string is a valid MAC address.
# A MAC address consists of six groups of two hexadecimal digits, separated by colons or hyphens.
# The hexadecimal digits can be either uppercase or lowercase.

import re

def is_valid_mac_address(mac_address):
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return re.match(pattern, mac_address) is not None

# Test the function
mac_address = input("Enter a MAC address: ")
print(is_valid_mac_address(mac_address))

# Example input: 00:1B:44:11:3A:B7
# Output: True
# Please Like and Subscribe