# We can calculate the Fibonacci sequence up to a certain number using a loop.
# First, we need to get the input from the user for the maximum number.
# Then, we initialize the first two numbers of the sequence as 0 and 1.
# We use a while loop to generate the Fibonacci sequence until the current number exceeds the maximum number.
# Inside the loop, we calculate the next number by adding the previous two numbers.
# We print each number in the sequence as it is generated.

max_number = int(input("Enter the maximum number: "))

# Initialize the first two numbers of the sequence
num1, num2 = 0, 1

# Print the first number
print(num1)

# Generate the Fibonacci sequence until the current number exceeds the maximum number
while num2 <= max_number:
    # Print the current number
    print(num2)
    # Calculate the next number by adding the previous two numbers
    num1, num2 = num2, num1 + num2

# Please Like and Subscribe