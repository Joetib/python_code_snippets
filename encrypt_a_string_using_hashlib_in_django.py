# Using hashlib library to encrypt a string in Django
# No need to install hashlib, it's included in Python

import hashlib

text = "Hello World"
# Encode the text before hashing
encoded_text = text.encode()
# Create a hashlib object with SHA-256 algorithm
hash_object = hashlib.sha256(encoded_text)
# Get the hexadecimal representation of the hash
hashed_text = hash_object.hexdigest()

print(hashed_text)
# Output
# >> 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'
# Please Like and Subscribe