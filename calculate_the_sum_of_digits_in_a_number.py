num = input("Enter a number: ")
# Convert the number to a string
num_str = str(num)
# Initialize the sum variable
sum_digits = 0
# Iterate through each digit in the number
for digit in num_str:
    # Convert the digit back to an integer and add it to the sum
    sum_digits += int(digit)
# Output the sum of digits
print(sum_digits)
# Please Like and Subscribe