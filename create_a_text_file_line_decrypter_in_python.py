# Let's create a simple text file line decrypter in Python
# We will read a text file, decrypt each line, and output the result

# Example text file 'encrypted.txt':
# Encrypted line 1
# Encrypted line 2

# First, let's install the cryptography library
# >> pip install cryptography

from cryptography.fernet import Fernet

# Generate a key using Fernet
key = Fernet.generate_key()
cipher = Fernet(key)

# Read the encrypted file
with open('encrypted.txt', 'r') as file:
    for line in file:
        encrypted_text = line.encode()
        decrypted_text = cipher.decrypt(encrypted_text).decode()
        print(decrypted_text)

# Output:
# Decrypted line 1
# Decrypted line 2
# Please Like and Subscribe