# We can use the `validate_email` function from the `validate_email` package to check if a string is a valid email domain.
# Install the `validate_email` package using:
# >> pip install validate_email

from validate_email_address import validate_email

email_domain = input("Enter email domain: ")

# Check if the email domain is valid
is_valid = validate_email(email_domain)

# Output the result
print(is_valid)

# Output
# >> True or False
# Please Like and Subscribe