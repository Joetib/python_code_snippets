# Use PyPDF2 library to extract text from a PDF file
# Install PyPDF2 using
# >> pip install PyPDF2

import PyPDF2

def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
    return text

# Usage
pdf_file_path = "path/to/your/pdf/file.pdf"
extracted_text = extract_text_from_pdf(pdf_file_path)
print(extracted_text)
# Please Like and Subscribe