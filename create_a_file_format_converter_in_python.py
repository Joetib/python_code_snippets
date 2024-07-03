# Use the python-docx library to convert .docx files to .pdf
# Install python-docx using
# >> pip install python-docx
from docx import Document

def convert_docx_to_pdf(input_file, output_file):
    doc = Document(input_file)
    doc.save(output_file)

# Example usage
input_file = "input.docx"
output_file = "output.pdf"
convert_docx_to_pdf(input_file, output_file)
# Please Like and Subscribe