# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.

def is_happy_number(num):
    # Create a set to store the seen numbers
    seen = set()
    
    # Loop until the number becomes 1 or it is seen again
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    
    # If the number becomes 1, it is a happy number
    return num == 1

# Test the function
print(is_happy_number(19))
# Output: True

print(is_happy_number(4))
# Output: False
# Please Like and Subscribe