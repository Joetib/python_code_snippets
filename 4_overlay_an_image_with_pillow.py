# To follow along, first make sure you have 'pillow' installed
# Type in your terminal: python -m pip install -U pillow

from PIL import Image

background_image = Image.open('background_image.png',)

color = (255, 0, 0, 154) # a RGBA red color with opacity of 60%
# You can specify any color you want.
# Now let's create our overlay image
overlay_image = Image.new(mode="RGBA", size=background_image.size, color=color)

# Now we write the overlay on top of the background from position (0,0)
background_image.paste(overlay_image, (0,0), overlay_image)

# Lets save a copy of our final image
background_image.save("final_overlayed_image.png", mode="PNG")
