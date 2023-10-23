# We can use the `validators` library to check if a string is a valid URL or IP address.
# Install the `validators` library using:
# >> pip install validators

import validators

# Let's define a function to check if a string is a valid URL
def is_valid_url(url):
    return validators.url(url)

# Let's define a function to check if a string is a valid IP address
def is_valid_ip(ip):
    return validators.ipv4(ip) or validators.ipv6(ip)

# Testing the functions
url = input("Enter a URL: ")
ip = input("Enter an IP address: ")

print(is_valid_url(url))
print(is_valid_ip(ip))

# Output
# True (if the URL is valid)
# True (if the IP address is valid)
# Please Like and Subscribe