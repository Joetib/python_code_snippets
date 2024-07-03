# Let's generate a random code snippet using the 'random' library
# Install 'random' using
# >> pip install random

import random
code = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=8))
# Let's output the generated code
print(code)
# Output
# >> e4a2g8h6
# Please Like and Subscribe