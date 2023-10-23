# We can use the `datetime` module in Python to check if a string is a valid time in the format `hh:mm:ss`.
# Here's how we can do it:

from datetime import datetime

time_str = input("Enter a time in the format hh:mm:ss: ")

try:
    datetime.strptime(time_str, "%H:%M:%S")
    print("Valid time format")
except ValueError:
    print("Invalid time format")

# Example input: "12:34:56"
# Output: Valid time format

# Example input: "12:34"
# Output: Invalid time format
# Please Like and Subscribe