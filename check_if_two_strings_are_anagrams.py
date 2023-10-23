# To check if two strings are anagrams, we can compare their sorted versions.
# If the sorted versions of the strings are equal, then the strings are anagrams.

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Sort the strings
sorted_string1 = sorted(string1)
sorted_string2 = sorted(string2)

# Check if the sorted strings are equal
if sorted_string1 == sorted_string2:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


# Please Like and Subscribe