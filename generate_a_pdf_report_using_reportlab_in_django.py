# Use reportlab library to generate a PDF report in Django
# Install reportlab using:
# >> pip install reportlab

from reportlab.pdfgen import canvas
from django.http import HttpResponse

def generate_pdf_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # Create a canvas object
    p = canvas.Canvas(response)

    # Add content to the PDF
    p.drawString(100, 800, "Hello, this is a PDF report!")

    # Save the PDF
    p.showPage()
    p.save()

    return response
# Please Like and Subscribe