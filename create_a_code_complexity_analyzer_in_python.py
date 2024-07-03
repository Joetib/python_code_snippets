# Use radon library to analyze code complexity
# Install radon using
# >> pip install radon

from radon.complexity import cc_rank, cc_visit
from radon.cli.tools import iter_filenames

# Define a function to calculate complexity
def calculate_complexity(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()
    # Calculate complexity
    results = cc_visit(source_code)
    return results

# Get list of Python files in a directory
file_paths = iter_filenames(['path/to/directory'], exclude='*test*.py')

# Loop through files and calculate complexity
for file_path in file_paths:
    complexity_results = calculate_complexity(file_path)
    print(f"File: {file_path}, Complexity: {complexity_results.total_complexity}")

# Output
# >> File: example.py, Complexity: 10
# >> File: another.py, Complexity: 15
# Please Like and Subscribe