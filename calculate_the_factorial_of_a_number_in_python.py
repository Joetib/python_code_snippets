# To calculate the factorial of a number, we can use a recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Let's test the factorial function
number = int(input("Enter a number: "))
result = factorial(number)
print("The factorial of", number, "is", result)
# Please Like and Subscribe