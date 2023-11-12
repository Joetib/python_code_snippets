# To create a URL shortener in Python, we can use the `pyshorteners` library.
# Install `pyshorteners` using:
# >> pip install pyshorteners

import pyshorteners

# Create an instance of the Shortener class
shortener = pyshorteners.Shortener()

# Enter the URL to be shortened
url = input("Enter the URL: ")

# Shorten the URL
shortened_url = shortener.tinyurl.short(url)

# Output the shortened URL
print(shortened_url)


# Please Like and Subscribe