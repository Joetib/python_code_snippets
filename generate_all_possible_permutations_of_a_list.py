# We can use the itertools module to generate all possible permutations of a list
# No need to install any third-party package

import itertools

# Define a list
lst = [1, 2, 3]

# Generate all permutations
permutations = list(itertools.permutations(lst))

# Output the permutations
print(permutations)

# Output
# >> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# Please Like and Subscribe