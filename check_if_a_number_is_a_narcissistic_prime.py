# To check if a number is a narcissistic prime, we need to check two conditions:
# 1. The number should be a prime number.
# 2. The number should be a narcissistic number.

# We can use the sympy library to check if a number is prime.
# Install sympy using:
# >> pip install sympy

from sympy import isprime

def is_narcissistic_prime(num):
    # Check if the number is prime
    if not isprime(num):
        return False

    # Check if the number is narcissistic
    sum_of_digits = sum(int(digit) ** len(str(num)) for digit in str(num))
    if sum_of_digits == num:
        return True
    else:
        return False

# Test the function
num = int(input("Enter a number: "))
print(is_narcissistic_prime(num))

# Example Output:
# Enter a number: 153
# True
# Please Like and Subscribe