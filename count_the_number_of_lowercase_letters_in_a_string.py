# We can use a simple loop to iterate through each character in the string
# and check if it is a lowercase letter using the islower() method.
# If it is, we increment a counter variable by 1.
# Finally, we print the value of the counter variable.

string = input("Enter a string: ")
count = 0

for char in string:
    if char.islower():
        count += 1

print(count)
# Please Like and Subscribe