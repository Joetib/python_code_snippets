# We can use the Luhn algorithm to check if a string is a valid credit card number.
# The Luhn algorithm works by summing up the digits of the credit card number in a specific way.
# If the sum is divisible by 10, then the credit card number is valid.

def is_valid_credit_card(number):
    # Remove any spaces or dashes from the credit card number
    number = number.replace(' ', '').replace('-', '')
    
    # Check if the number is a valid integer
    if not number.isdigit():
        return False
    
    # Reverse the credit card number
    reversed_number = number[::-1]
    
    # Initialize the sum
    total = 0
    
    # Iterate over the reversed number
    for i, digit in enumerate(reversed_number):
        # Convert the digit to an integer
        digit = int(digit)
        
        # Double every second digit
        if i % 2 == 1:
            digit *= 2
            
            # If the doubled digit is greater than 9, subtract 9
            if digit > 9:
                digit -= 9
        
        # Add the digit to the total
        total += digit
    
    # Check if the total is divisible by 10
    if total % 10 == 0:
        return True
    else:
        return False

# Test the function
credit_card_number = input("Enter credit card number: ")
print(is_valid_credit_card(credit_card_number))

# Example usage:
# Enter credit card number: 4111 1111 1111 1111
# True
# Please Like and Subscribe