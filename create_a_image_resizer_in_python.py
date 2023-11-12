# To resize an image in Python, we can use the `PIL` (Python Imaging Library) package.
# Install PIL using:
# >> pip install pillow

from PIL import Image

# Open the image file
image = Image.open("input_image.jpg")

# Set the desired width and height for the resized image
width = 500
height = 300

# Resize the image
resized_image = image.resize((width, height))

# Save the resized image
resized_image.save("output_image.jpg")

# Output
# The input_image.jpg will be resized to 500x300 pixels and saved as output_image.jpg
# Please Like and Subscribe