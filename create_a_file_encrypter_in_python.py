# Let's create a file encrypter in Python using the cryptography package
# Install cryptography using
# >> pip install cryptography

from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
# Create a Fernet object with the generated key
cipher = Fernet(key)
# Specify the path of the file to be encrypted
file_path = input("Enter the path of the file to encrypt: ")
# Read the contents of the file
with open(file_path, 'rb') as file:
    file_data = file.read()
# Encrypt the file data
encrypted_data = cipher.encrypt(file_data)
# Specify the path to save the encrypted file
encrypted_file_path = input("Enter the path to save the encrypted file: ")
# Write the encrypted data to the file
with open(encrypted_file_path, 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)