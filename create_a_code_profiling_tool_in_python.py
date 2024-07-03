# Use cProfile to profile code execution time
import cProfile

def my_function():
    total = 0
    for i in range(1000):
        total += i
    return total

# Profile the function
cProfile.run('my_function()')

# Output:
# 2 function calls in 0.000 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# Please Like and Subscribe