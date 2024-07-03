# Django provides EmailValidator to validate email addresses
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

email = "example@example.com"
validator = EmailValidator()
try:
    validator(email)
    print("Email is valid")
except ValidationError:
    print("Email is invalid")
# Output
# >> Email is valid
# Please Like and Subscribe