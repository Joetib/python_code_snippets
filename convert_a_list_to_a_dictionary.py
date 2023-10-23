# To convert a list to a dictionary, we can use the `zip` function.
# The `zip` function takes two or more iterables and returns an iterator
# of tuples, where the i-th tuple contains the i-th element from each of
# the input iterables.

# Here's an example of how to convert a list to a dictionary:

my_list = ['apple', 'banana', 'orange']
my_dict = dict(zip(range(len(my_list)), my_list))

print(my_dict)

# Output:
# {0: 'apple', 1: 'banana', 2: 'orange'}
# Please Like and Subscribe