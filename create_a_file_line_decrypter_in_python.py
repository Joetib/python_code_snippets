# Let's create a file line decrypter in Python
# We will read a file, decrypt each line, and write to a new file
# Let's use cryptography library for decryption
# Install cryptography using
# >> pip install cryptography

from cryptography.fernet import Fernet
# Generate a key for encryption/decryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Read encrypted file
with open('encrypted_file.txt', 'rb') as file:
    encrypted_data = file.read()

# Decrypt each line
decrypted_data = cipher.decrypt(encrypted_data)

# Write decrypted data to a new file
with open('decrypted_file.txt', 'wb') as file:
    file.write(decrypted_data)
# Output: decrypted_file.txt will contain decrypted data
# Please Like and Subscribe