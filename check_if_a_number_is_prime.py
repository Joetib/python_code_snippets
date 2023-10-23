# To check if a number is prime, we can iterate from 2 to the square root of the number and check if the number is divisible by any of the numbers in that range.
# If the number is divisible by any number in that range, then it is not prime. Otherwise, it is prime.

import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Test the function
number = int(input("Enter a number: "))
print(is_prime(number))

# Output
# >> True (if the number is prime)
# >> False (if the number is not prime)
# Please Like and Subscribe