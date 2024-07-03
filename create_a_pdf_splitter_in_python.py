# To split a PDF file into multiple smaller PDF files, we can use the PyPDF2 library.
# Install PyPDF2 using pip:
# >> pip install PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
pdf_file = open('input.pdf', 'rb')
pdf_reader = PdfFileReader(pdf_file)
total_pages = pdf_reader.numPages
for page_number in range(total_pages):
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf_reader.getPage(page_number))
    # Create a new PDF file for the current page
    output_pdf = open(f'output_page_{page_number + 1}.pdf', 'wb')
    # Write the PDF writer object to the output PDF file
    pdf_writer.write(output_pdf)
    # Close the output PDF file
    output_pdf.close()

# Close the input PDF file
pdf_file.close()
# Please Like and Subscribe