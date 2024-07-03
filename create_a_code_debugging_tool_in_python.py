# Use built-in module 'pdb' for Python code debugging
import pdb

def add(a, b):
    # Set a breakpoint
    pdb.set_trace()
    return a + b

result = add(5, 3)
print(result)

# Debugging commands:
# c - continue execution
# n - step to the next line
# s - step into a function
# l - list source code
# p - print variable value
# q - quit debugger
# h - help on commands
# Please Like and Subscribe