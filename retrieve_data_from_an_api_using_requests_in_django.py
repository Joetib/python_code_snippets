# Let's use requests library to fetch data from an API
# Install requests using
# >> pip install requests

import requests

url = "https://api.example.com/data"
response = requests.get(url)
data = response.json()
# Now 'data' contains the fetched data from the API
# Please Like and Subscribe