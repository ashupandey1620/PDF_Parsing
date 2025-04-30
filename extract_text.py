import fitz

pdf = fitz.open(r"C:\Users\ashup\OneDrive\Desktop\PDF Parsing\Ruskin - Immortal Stories.pdf")
print(pdf.page_count)

page = pdf.load_page(9)
text = page.gettext('text')

pdf.close()

from PyPDF2 import PdfReader

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text() or ''
    return text
