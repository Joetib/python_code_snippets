# We can remove vowels from a string by iterating over each character in the string and checking if it is a vowel. If it is not a vowel, we add it to a new string. Finally, we return the new string without vowels.

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string

# Example usage
text = input("Enter a string: ")
print(remove_vowels(text))

# Input: "Hello World"
# Output: "Hll Wrld"
# Please Like and Subscribe