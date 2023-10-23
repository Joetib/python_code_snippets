# To calculate the factorial of a large number using recursion,
# we can define a recursive function that multiplies the number
# with the factorial of the number minus one.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
number = int(input("Enter a number: "))
result = factorial(number)
print(result)

# Output
# Enter a number: 5
# 120
# Please Like and Subscribe