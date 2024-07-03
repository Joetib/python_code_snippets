# To create a file decrypter in Python, we can use the cryptography package.
# Install cryptography using:
# >> pip install cryptography
from cryptography.fernet import Fernet
# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher = Fernet(key)
def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        encrypted_data = cipher.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)
def decrypt_file(file_path):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)
# Usage example
file_path = 'encrypted_file.txt'
encrypt_file(file_path)
decrypt_file(file_path)