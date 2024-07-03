# Use pylint library to analyze Python code for errors and style
# Install pylint using
# >> pip install pylint

import pylint.lint
# Analyze a Python file named 'example.py'
pylint_opts = ['example.py']
pylint.lint.Run(pylint_opts)
# Output
# >> No errors or warnings found
# Please Like and Subscribe