from PyPDF2 import PdfReader

def get_pdf_metadata(pdf_path):
    reader = PdfReader(pdf_path)
    return reader.metadata