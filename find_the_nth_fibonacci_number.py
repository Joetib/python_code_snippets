# To find the nth Fibonacci number, we can use a recursive approach.
# The Fibonacci sequence starts with 0 and 1, and each subsequent number
# is the sum of the two preceding ones.

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the value of n: "))
print(fibonacci(n))

# Example input: n = 6
# Output: 5

# Example input: n = 10
# Output: 34
# Please Like and Subscribe