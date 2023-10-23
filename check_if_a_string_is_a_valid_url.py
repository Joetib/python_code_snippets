# We can use the `urllib.parse` module in Python to check if a string is a valid URL.
# This module provides functions for parsing URLs and manipulating URL components.

from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Let's test the function with some examples

print(is_valid_url("https://www.example.com"))
# Output: True

print(is_valid_url("www.example.com"))
# Output: False

print(is_valid_url("example.com"))
# Output: False

print(is_valid_url("https://www.example.com/path?query=string"))
# Output: True

print(is_valid_url("https://www.example.com/path#fragment"))
# Output: True

print(is_valid_url("ftp://ftp.example.com"))
# Output: True

print(is_valid_url("invalid url"))
# Output: False
# Please Like and Subscribe