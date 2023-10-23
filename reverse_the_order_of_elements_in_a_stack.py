# To reverse the order of elements in a stack, we can use an auxiliary stack.

# Let's assume we have a stack called 'stack' with elements [1, 2, 3, 4, 5].

# We will pop each element from the original stack and push it onto the auxiliary stack.
# This will reverse the order of elements in the auxiliary stack.

# Finally, we will pop each element from the auxiliary stack and push it back onto the original stack.
# This will reverse the order of elements in the original stack.

# Here's the code:

stack = [1, 2, 3, 4, 5]  # Original stack

aux_stack = []  # Auxiliary stack

# Reverse the order of elements using auxiliary stack
while stack:
    aux_stack.append(stack.pop())

# Push the elements back to the original stack
while aux_stack:
    stack.append(aux_stack.pop())

print(stack)
# Output: [5, 4, 3, 2, 1]
# Please Like and Subscribe