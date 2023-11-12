# To create a web crawler in Python, we can use the `requests` and `BeautifulSoup` libraries.
# Install the required libraries using:
# >> pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
url = "https://example.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
# Find all the links on the webpage
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

# Output:
# https://example.com/page1
# https://example.com/page2

# Note: This is a basic example of a web crawler that extracts all the links from a webpage.
# You can modify and extend this code to perform more complex crawling tasks, such as scraping 
# data or following links recursively.
# Please Like and Subscribe