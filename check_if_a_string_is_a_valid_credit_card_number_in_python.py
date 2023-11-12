# We can use the `creditcard` package to check if a string is a valid credit card number.
# Install the package using:
# >> pip install creditcard

from creditcard import CreditCard

credit_card_number = input("Enter credit card number: ")

# Create a CreditCard object
cc = CreditCard(credit_card_number)

# Check if the credit card number is valid
is_valid = cc.is_valid()

# Output the result
print(is_valid)


# Please Like and Subscribe