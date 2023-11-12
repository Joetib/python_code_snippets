# To generate PDFs in Python, we can use the `reportlab` library.
# Install `reportlab` using:
# >> pip install reportlab

from reportlab.pdfgen import canvas

# Create a new PDF file
pdf = canvas.Canvas("output.pdf")

# Set the font and font size
pdf.setFont("Helvetica", 12)

# Add text to the PDF
pdf.drawString(100, 700, "Hello, World!")

# Save the PDF file
pdf.save()

# Output
# A PDF file named "output.pdf" will be generated with the text "Hello, World!"
# Please Like and Subscribe