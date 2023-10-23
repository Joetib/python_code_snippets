# We can use a simple loop to iterate through each character in the string
# and check if it is an uppercase letter using the isupper() method.
# If it is, we increment a counter variable.

string = input("Enter a string: ")
count = 0

for char in string:
    if char.isupper():
        count += 1

print(count)
# Please Like and Subscribe