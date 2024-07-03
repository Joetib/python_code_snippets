# Generate a random string in Django using the get_random_string method
# No need to install any additional packages

from django.utils.crypto import get_random_string
random_string = get_random_string(length=10)
# Output a random string with length 10 characters
print(random_string)
# Output
# >> '2wP4jR7oDf'
# Please Like and Subscribe