# We can use the random module in Python to generate random numbers
import random

# Generate a random integer between a given range
random_number = random.randint(1, 100)
print(random_number)

# Generate a random float between 0 and 1
random_float = random.random()
print(random_float)

# Generate a random element from a list
my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print(random_element)

# Shuffle the elements in a list randomly
random.shuffle(my_list)
print(my_list)
# Please Like and Subscribe