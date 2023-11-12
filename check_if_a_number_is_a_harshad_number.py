# A Harshad number is a number that is divisible by the sum of its digits.
# To check if a number is a Harshad number, we need to calculate the sum of its digits
# and check if the number is divisible by the sum.

def is_harshad_number(number):
    # Convert the number to a string to iterate over its digits
    digits = str(number)
    
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in digits)
    
    # Check if the number is divisible by the sum of its digits
    if number % digit_sum == 0:
        return True
    else:
        return False

# Test the function
number = int(input("Enter a number: "))
print(is_harshad_number(number))

# Example usage:
# Enter a number: 18
# True
# Please Like and Subscribe