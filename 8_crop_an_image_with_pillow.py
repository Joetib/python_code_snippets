# First make sure you have pillow installed by running
# "pip install -U pillow"
from PIL import Image

# Lets define the coordinates we want to crop to
coordinates = (300, 100, 900, 500)

# Let's open our image file. For Example: `path_to_image.png`
image = Image.open("path_to_image.png") 

cropped_image = image.crop(coordinates)

# Let's save the image to `output_image.png``
cropped_image.save("output_image.png")

# Please Like and subscribe.