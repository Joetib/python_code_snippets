# We can use the `ipaddress` module from the Python standard library to check if a string is a valid IPv4 address.
# No additional installation is required.

import ipaddress

def is_valid_ipv4(address):
    try:
        ipaddress.IPv4Address(address)
        return True
    except ipaddress.AddressValueError:
        return False

# Example usage:
address = input("Enter an IPv4 address: ")
print(is_valid_ipv4(address))

# Output:
# Enter an IPv4 address: 192.168.0.1
# True
# Please Like and Subscribe