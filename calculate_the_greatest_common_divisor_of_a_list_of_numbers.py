# We can use the math module's gcd function to calculate the greatest common divisor (GCD) of two numbers.
# To find the GCD of a list of numbers, we can iterate through the list and calculate the GCD of each pair of numbers.
# We can start by assuming the GCD as the first number in the list, and then update it with the GCD of the next number and the current GCD.
# Finally, the GCD of the entire list will be stored in the variable.

# Let's write the code:

# import the math module
import math

# define a function to calculate the GCD of a list of numbers
def calculate_gcd(numbers):
    # assume the GCD as the first number in the list
    gcd = numbers[0]
    
    # iterate through the list starting from the second number
    for num in numbers[1:]:
        # calculate the GCD of the current number and the current GCD
        gcd = math.gcd(gcd, num)
    
    # return the final GCD
    return gcd

# example usage
numbers = [12, 18, 24, 36]
print(calculate_gcd(numbers))

# Output:
# 6
# Please Like and Subscribe