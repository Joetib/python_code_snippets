# We can use the re module to convert a string to kebab case
import re

def to_kebab_case(string):
    # Replace all non-alphanumeric characters with a hyphen
    kebab_case_string = re.sub(r'[^a-zA-Z0-9]', '-', string)
    # Convert the string to lowercase
    kebab_case_string = kebab_case_string.lower()
    # Remove leading and trailing hyphens
    kebab_case_string = kebab_case_string.strip('-')
    # Replace multiple consecutive hyphens with a single hyphen
    kebab_case_string = re.sub(r'-+', '-', kebab_case_string)
    
    return kebab_case_string

# Example usage
string = input("Enter a string: ")
kebab_case_string = to_kebab_case(string)
print(kebab_case_string)
# Please Like and Subscribe