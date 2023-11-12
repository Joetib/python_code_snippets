# To sort a dictionary by its values, we can use the `sorted` function
# along with a lambda function as the `key` parameter.
# The lambda function will return the value of each key-value pair
# in the dictionary, which will be used for sorting.

# Example dictionary
my_dict = {'a': 5, 'b': 2, 'c': 10, 'd': 1}

# Sort the dictionary by values in ascending order
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

print(sorted_dict)

# Output:
# {'d': 1, 'b': 2, 'a': 5, 'c': 10}
# Please Like and Subscribe