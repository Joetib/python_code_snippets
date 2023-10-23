# To count the number of special characters in a string, we can use a regular expression to match all special characters and then count the number of matches.

import re

def count_special_characters(string):
    # Define the pattern for special characters
    pattern = r"[^\w\s]"
    
    # Use re.findall() to find all matches of the pattern in the string
    matches = re.findall(pattern, string)
    
    # Return the count of matches
    return len(matches)

# Test the function
string = input("Enter a string: ")
count = count_special_characters(string)
print(count)

# Example Input
# Enter a string: Hello! How are you?
# Output
# 1

# Example Input
# Enter a string: @#$%^&*()
# Output
# 8
# Please Like and Subscribe