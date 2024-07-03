# Let's use cryptography library to encrypt file content
# Install cryptography using
# >> pip install cryptography

from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt file content
with open('file.txt', 'rb') as file:
    data = file.read()
encrypted_data = cipher.encrypt(data)

# Write encrypted content back to file
with open('file.txt', 'wb') as file:
    file.write(encrypted_data)

# To decrypt the content, use:
# decrypted_data = cipher.decrypt(encrypted_data)
# Please Like and Subscribe