# Use the 'autopep8' library to automatically format Python code
# Install 'autopep8' using:
# >> pip install autopep8

import autopep8

# Define a function that takes in a file path and refactors the code
def refactor_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
        # Use autopep8 to refactor the code
        refactored_code = autopep8.fix_code(code)
    
    # Write the refactored code back to the file
    with open(file_path, 'w') as file:
        file.write(refactored_code)

# Provide the file path of the Python file to be refactored
file_path = 'example.py'
refactor_code(file_path)
# Please Like and Subscribe