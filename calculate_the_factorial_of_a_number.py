# To calculate the factorial of a number, we can use a recursive function.
# The factorial of a number n is the product of all positive integers less than or equal to n.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Let's test the factorial function with an example
number = int(input("Enter a number: "))
result = factorial(number)
print(result)

# Output:
# Enter a number: 5
# 120
# Please Like and Subscribe