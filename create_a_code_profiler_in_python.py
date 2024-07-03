# Use cProfile to profile the code execution time
import cProfile

def my_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

# Create a profile object
profiler = cProfile.Profile()
# Enable profiling
profiler.enable()
# Call the function to profile
result = my_function()
# Disable profiling
profiler.disable()
# Print the profiling results
profiler.print_stats()
# Please Like and Subscribe