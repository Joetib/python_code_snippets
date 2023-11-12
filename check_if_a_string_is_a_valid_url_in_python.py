# We can use the `urllib.parse` module in Python to check if a string is a valid URL.
# Here is a code snippet that demonstrates how to do it:

from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Example usage:
url = input("Enter a URL: ")
if is_valid_url(url):
    print("Valid URL")
else:
    print("Invalid URL")

# Output:
# Enter a URL: https://www.example.com
# Valid URL
# Please Like and Subscribe