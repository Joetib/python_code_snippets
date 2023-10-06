# Lets download files using requests. First install using
# >>> pip install requests

import requests

url = "https://example.com/examplefile.png"

# Let's open the link
r = requests.get(url)

# Now we save the content into a bile of out choosing.
with open ("examplefile.png", "wb") as f:
    f.write(r.content)

# Please Like, Subscribe and Share.     
