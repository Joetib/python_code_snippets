# We can solve this problem by iterating through all possible pairs of numbers and checking if their product is a palindrome.
# We start with the largest possible numbers and decrement them until we find a palindrome product.

largest_palindrome = 0

# Iterate through all possible pairs of numbers
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        # Calculate the product
        product = i * j
        
        # Check if the product is a palindrome
        if str(product) == str(product)[::-1]:
            # Update the largest palindrome if necessary
            if product > largest_palindrome:
                largest_palindrome = product

# Output the largest palindrome product
print(largest_palindrome)


# Please Like and Subscribe