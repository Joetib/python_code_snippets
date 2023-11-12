# An abundant number is a number for which the sum of its proper divisors is greater than the number itself.
# To check if a number is an abundant number, we need to find the sum of its proper divisors and compare it with the number itself.

def is_abundant_number(num):
    # Find the sum of proper divisors
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    
    # Check if the sum of proper divisors is greater than the number
    if divisors_sum > num:
        return True
    else:
        return False

# Test the function
num = int(input("Enter a number: "))
print(is_abundant_number(num))

# Example Output
# Enter a number: 12
# True
# Please Like and Subscribe