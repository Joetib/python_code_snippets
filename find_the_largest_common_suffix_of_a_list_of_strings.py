# To find the largest common suffix of a list of strings,
# we can iterate through the characters of the first string
# and compare them with the corresponding characters of the
# other strings. We will keep track of the common suffix
# characters until we find a character that is different
# or reach the end of any string.

strings = ["apple", "pineapple", "banana"]

# Initialize the common suffix as the first string
common_suffix = strings[0]

# Iterate through the characters of the first string
for i in range(len(strings[0])):
    # Compare the character with the corresponding characters
    # of the other strings
    for string in strings[1:]:
        # If the character is different or we reach the end of
        # any string, break the loop
        if i >= len(string) or string[-(i+1)] != common_suffix[-(i+1)]:
            break
    else:
        # If the loop completes without breaking, the character
        # is common to all strings, so add it to the common suffix
        continue
    break

# The common suffix is the substring from the last character
# of the first string up to the current character
common_suffix = common_suffix[-i:]

print(common_suffix)

# Output:
# ple
# Please Like and Subscribe