# Use Pillow library to resize and crop an image in Django
# Install Pillow using
# >> pip install Pillow

from PIL import Image

# Open an image file
img = Image.open('image.jpg')

# Resize the image to 300x300
img_resized = img.resize((300, 300))

# Crop the image to a 100x100 square starting at coordinates (50, 50)
img_cropped = img_resized.crop((50, 50, 150, 150))

# Save the cropped image
img_cropped.save('cropped_image.jpg')

# Output
# A new image 'cropped_image.jpg' will be saved
# Please Like and Subscribe