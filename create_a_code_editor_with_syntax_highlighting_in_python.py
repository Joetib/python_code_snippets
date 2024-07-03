# Use Pygments library for syntax highlighting in a code editor
# Install Pygments using
# >> pip install Pygments

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter

code = '''
def greet():
    print("Hello, World!")
'''

lexer = get_lexer_by_name("python", stripall=True)
formatter = TerminalFormatter()
highlighted_code = highlight(code, lexer, formatter)

# Let's output the syntax highlighted code
print(highlighted_code)
# Please Like and Subscribe