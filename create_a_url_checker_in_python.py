# We can use the `requests` library to check if a URL is valid and accessible.
# Install requests using:
# >> pip install requests

import requests
def check_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False
# Let's test the function with a URL
url = input("Enter URL: ")
if check_url(url):
    print("URL is valid and accessible")
else:
    print("URL is invalid or not accessible")
# Output
# >> Enter URL: https://www.google.com
# >> URL is valid and accessible
# Please Like and Subscribe