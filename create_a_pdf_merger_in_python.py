# To merge multiple PDF files into a single PDF file, we can use the PyPDF2 library.
# Install PyPDF2 using pip:
# >> pip install PyPDF2

from PyPDF2 import PdfMerger

# Create an instance of PdfMerger
merger = PdfMerger()

# Add the PDF files to be merged
merger.append('file1.pdf')
merger.append('file2.pdf')
merger.append('file3.pdf')

# Specify the output file name
output_file = 'merged.pdf'

# Merge the PDF files
merger.write(output_file)

# Close the merger
merger.close()

# Output
# A new PDF file named 'merged.pdf' will be created,
# containing the merged content of 'file1.pdf', 'file2.pdf', and 'file3.pdf'.
# Please Like and Subscribe