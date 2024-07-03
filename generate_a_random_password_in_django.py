# Using Django's get_random_string to generate a random password
# No need to install any additional packages

from django.utils.crypto import get_random_string
password = get_random_string(length=12)
# Output
# >> 'x7Kj9P3sL6Rt'
# Please Like and Subscribe