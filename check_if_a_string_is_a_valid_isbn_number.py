# We can use the `isbnlib` library to check if a string is a valid ISBN number.
# Install `isbnlib` using:
# >> pip install isbnlib

import isbnlib

isbn = input("Enter ISBN number: ")
valid = isbnlib.is_isbn10(isbn) or isbnlib.is_isbn13(isbn)

print(valid)

# Please Like and Subscribe