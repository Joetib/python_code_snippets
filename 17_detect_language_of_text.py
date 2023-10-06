# Let's use langdetect library to find the language of a provided text
# install langdetect using
# >> pip install langdetect

from langdetect import detect

text = input("Enter text whose language you want to know: ")

# Let's output the language
print(detect(text))

# easy right（^—^）