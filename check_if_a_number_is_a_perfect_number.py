# A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself).
# To check if a number is a perfect number, we can find all the proper divisors of the number and sum them up.
# If the sum is equal to the number itself, then it is a perfect number.

def is_perfect_number(num):
    # Find all the proper divisors of the number
    divisors = [i for i in range(1, num) if num % i == 0]
    
    # Sum up the divisors
    divisor_sum = sum(divisors)
    
    # Check if the sum is equal to the number
    if divisor_sum == num:
        return True
    else:
        return False

# Test the function
number = int(input("Enter a number: "))
print(is_perfect_number(number))

# Example Output:
# Enter a number: 6
# True
# Please Like and Subscribe