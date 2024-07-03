# Let's create a text file line encrypter in Python
# Install cryptography library using
# >> pip install cryptography

from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt each line in the text file
with open('input.txt', 'r') as file:
    lines = file.readlines()
    encrypted_lines = [cipher.encrypt(line.encode()) for line in lines]

# Write the encrypted lines to a new file
with open('encrypted.txt', 'w') as file:
    for encrypted_line in encrypted_lines:
        file.write(encrypted_line.decode() + '\n')

# Output
# input.txt contains:
# Hello, World!
# Python is awesome.
# encrypted.txt will contain the encrypted lines
# Please Like and Subscribe