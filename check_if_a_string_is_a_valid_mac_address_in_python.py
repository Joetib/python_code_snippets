# We can use a regular expression to check if a string is a valid MAC address.
# A MAC address consists of six groups of two hexadecimal digits, separated by colons or hyphens.
# The regular expression pattern to match a valid MAC address is:
# ^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$

import re

def is_valid_mac_address(mac_address):
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return re.match(pattern, mac_address) is not None

# Example usage
mac_address = input("Enter MAC address: ")
print(is_valid_mac_address(mac_address))

# Output
# >> Enter MAC address: 00:1B:44:11:3A:B7
# >> True
# Please Like and Subscribe