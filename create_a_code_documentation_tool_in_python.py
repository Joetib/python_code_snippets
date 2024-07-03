# Use pdoc3 library to generate documentation for Python code
# Install pdoc3 using:
# >> pip install pdoc3

import os
import subprocess

def generate_documentation(input_file):
    """
    Generate HTML documentation for a Python file using pdoc3.
    
    Args:
    input_file (str): Path to the Python file for which documentation is needed.
    """
    output_dir = "docs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Generate documentation using pdoc3
    subprocess.run(["pdoc", "--html", input_file, "-o", output_dir])

# Example usage
generate_documentation("example.py")
# This will create HTML documentation in the 'docs' folder
# Please Like and Subscribe