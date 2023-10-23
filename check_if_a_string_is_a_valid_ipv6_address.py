# We can use the `ipaddress` module from the Python standard library to check if a string is a valid IPv6 address.
# No additional installation is required.

import ipaddress

def is_valid_ipv6(address):
    try:
        ipaddress.IPv6Address(address)
        return True
    except ipaddress.AddressValueError:
        return False

# Example usage
address = input("Enter an IPv6 address: ")
print(is_valid_ipv6(address))

# Output
# >> Enter an IPv6 address: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
# >> True
# Please Like and Subscribe