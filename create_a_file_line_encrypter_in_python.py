# Let's create a file line encrypter in Python
# Install cryptography library using
# >> pip install cryptography

from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt a line
line = b"Hello, this is a secret message"
encrypted_line = cipher.encrypt(line)
print("Encrypted line:", encrypted_line)

# Decrypt the line
decrypted_line = cipher.decrypt(encrypted_line)
print("Decrypted line:", decrypted_line.decode())
# Please Like and Subscribe