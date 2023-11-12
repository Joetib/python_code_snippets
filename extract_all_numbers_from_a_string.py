# We can use regular expressions to extract all numbers from a string
# First, we need to import the re module
import re

# Let's define a function that takes a string as input and returns a list of numbers
def extract_numbers(string):
    # Use the findall() function from the re module to find all numbers in the string
    numbers = re.findall(r'\d+', string)
    return numbers

# Let's test the function with a sample string
string = "I have 10 apples and 5 oranges"
numbers = extract_numbers(string)
print(numbers)
# Output
# >> ['10', '5']
# Please Like and Subscribe