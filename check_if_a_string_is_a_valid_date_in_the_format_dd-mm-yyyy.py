# We can use the `datetime` module in Python to check if a string is a valid date in the format dd-mm-yyyy.
# The `datetime.strptime()` function can be used to parse a string into a datetime object using a specified format.

from datetime import datetime

date_string = input("Enter a date (dd-mm-yyyy): ")

try:
    datetime.strptime(date_string, "%d-%m-%Y")
    print("Valid date")
except ValueError:
    print("Invalid date")

# Output
# >> Enter a date (dd-mm-yyyy): 31-12-2022
# >> Valid date
# Please Like and Subscribe