# We can use the `permutations` function from the `itertools` module to generate all permutations of a string.
# The `permutations` function returns an iterator that produces tuples containing all possible permutations of the input iterable.

# Let's define a function `get_permutations` that takes a string as input and returns a list of all permutations.

# Example usage:
# get_permutations("abc")
# Output:
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

from itertools import permutations

def get_permutations(string):
    return [''.join(p) for p in permutations(string)]

# Test the function
print(get_permutations("abc"))
# Please Like and Subscribe