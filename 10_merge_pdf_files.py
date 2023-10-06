# Let's merge pdf files using PyMuPD. Install it using
# >>> pip install PyMuPDF

import fitz as pdf

# For this example I will use three pdf files.
old_pdf_files_to_merge = ['file1.pdf', 'file2.pdf', "file3.pdf"]

# Now lets create a new pdf file
new_pdf = pdf.open()

# Now we add each file to our newly created pdf.
for filename in old_pdf_files_to_merge:
    with pdf.open(filename) as file:
        new_pdf.insertPDF(file)

# Now let's save the file to disk
new_pdf.save("new_pdf_file.pdf")

# Please Like, Subscribe and Share
