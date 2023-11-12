# A Kaprekar number is a number whose square can be split into two parts
# that add up to the original number.

def is_kaprekar_number(num):
    square = num ** 2
    num_str = str(square)
    for i in range(1, len(num_str)):
        left_part = int(num_str[:i])
        right_part = int(num_str[i:])
        if left_part + right_part == num:
            return True
    return False

# Test the function
num = int(input("Enter a number: "))
print(is_kaprekar_number(num))

# Example Output:
# Enter a number: 9
# True
# Please Like and Subscribe