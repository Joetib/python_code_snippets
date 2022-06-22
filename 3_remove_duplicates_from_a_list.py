# Now let's remove duplicate values from a list
# Here's our list example for today


list_with_duplicates = [1, 1, 2, 3, 4, 4, 3, 3, 5, 5, 6, 6, 'a', 'b', 'a', 'b']
"""
So this is a multiline comment 
Just to test out the spacing problem
and also to test the height it can get to.
"""
# The data structure SET avoids duplicate values
# Let's use it to remove duplicates


list_without_duplicates = list(set(list_with_duplicates))

print(list_without_duplicates)

# OUTPUT >>> [1, 2, 3, 4, 5, 6, 'a', 'b']