# Let's share files to our friends using gofile.io
# First install the gofile package using
# >>> pip install gofile

import gofile


def store_file(file):
    url = gofile.uploadFile(file)
    print("Download Link: ", url["downloadPage"])


# test this with a file using
store_file("filename.pdf")
