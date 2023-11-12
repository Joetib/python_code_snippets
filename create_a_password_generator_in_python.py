# We can use the `secrets` module in Python to generate secure random passwords.
# The `secrets` module provides functions for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

# Let's import the `secrets` module
import secrets

# Define the characters that can be used in the password
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-"

# Define the length of the password
length = 10

# Generate a random password using the defined characters and length
password = ''.join(secrets.choice(characters) for _ in range(length))

# Output the generated password
print(password)

# Output
# >> 8J@6&v3q9K
# Please Like and Subscribe