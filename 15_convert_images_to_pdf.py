# We will convert a list of images to pdf using pillow. install pillow using
# >> pip install pillow

from PIL import Image


def images_to_pdf(filenames: list[str], output_filename: str):
    images: list[Image.Image] = []
    for file in filenames:
        im = Image.open(file)
        im = im.convert("RGB")
        images.append(im)
    images[0].save(output_filename, save_all=True, append_images=images[1:])


# Let's test this with some images
images_to_pdf(filenames=["file1.png", "file2.png"], output_filename="output.pdf")
