# Let's convert numbers to bytecode using python-barcode.
# Install python-barcode using
# >> pip install python-barcode

import barcode
from barcode.writer import ImageWriter

number = input("Enter the text to generate barcode: ")

# get the barcode format
barcode_format = barcode.get_barcode_class("upc")
my_barcode = barcode_format(number, writer=ImageWriter())

# save to a file
my_barcode.save("generated_barcode")
