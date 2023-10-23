# We can use a list comprehension to filter out the even numbers from the list
# and then use the sum() function to find the sum of the filtered numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use list comprehension to filter out even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

# Find the sum of the even numbers
sum_of_even_numbers = sum(even_numbers)

print(sum_of_even_numbers)

# Output
# >> 30
# Please Like and Subscribe