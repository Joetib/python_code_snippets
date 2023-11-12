# To check if a number is a perfect power, we can use a brute force approach.
# We start with the base number 2 and keep increasing it until the base raised to some power is greater than the given number.
# If at any point, the base raised to some power is equal to the given number, then the number is a perfect power.
# Otherwise, the number is not a perfect power.

def is_perfect_power(num):
    base = 2
    while base ** 2 <= num:
        power = 2
        while base ** power <= num:
            if base ** power == num:
                return True
            power += 1
        base += 1
    return False

# Example usage
number = int(input("Enter a number: "))
print(is_perfect_power(number))

# Output
# >> Enter a number: 16
# >> True
# Please Like and Subscribe