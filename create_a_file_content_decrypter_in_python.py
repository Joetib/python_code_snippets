# Let's use cryptography library to decrypt a file content
# Install cryptography using
# >> pip install cryptography

from cryptography.fernet import Fernet

# Load the key from a file
with open('key.key', 'rb') as f:
    key = f.read()

cipher = Fernet(key)

# Read encrypted file content
with open('encrypted_file.txt', 'rb') as f:
    encrypted_data = f.read()

# Decrypt the content
decrypted_data = cipher.decrypt(encrypted_data)

# Write decrypted content to a new file
with open('decrypted_file.txt', 'wb') as f:
    f.write(decrypted_data)
# Please Like and Subscribe