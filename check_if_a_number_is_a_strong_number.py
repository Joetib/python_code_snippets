# A strong number is a number whose sum of the factorial of its digits
# is equal to the number itself.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def is_strong_number(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Calculate the sum of the factorial of each digit
    digit_sum = sum(factorial(int(digit)) for digit in num_str)
    
    # Check if the sum is equal to the number
    if digit_sum == num:
        return True
    else:
        return False

# Test the function
num = int(input("Enter a number: "))
print(is_strong_number(num))
# Please Like and Subscribe