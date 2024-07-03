# Use the 'pyminifier' library to obfuscate Python code
# Install pyminifier using:
# >> pip install pyminifier

from pyminifier import minification
code = """
def hello():
    print("Hello, World!")
hello()
"""
# Obfuscate the code
obfuscated_code = minification.remove_comments_and_docstrings(code)
print(obfuscated_code)
# Output
# >> def hello():print("Hello, World!");hello()
# Please Like and Subscribe