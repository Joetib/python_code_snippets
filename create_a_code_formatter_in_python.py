# Use black library for code formatting
# Install black using
# >> pip install black

import black

code = """
def   example   (   )  :
    print  (  "Hello, World!"  )
"""

# Format the code
formatted_code = black.format_file_contents(code, fast=False, mode=black.FileMode())

print(formatted_code)
# Output
# def example():
#     print("Hello, World!")
# Please Like and Subscribe