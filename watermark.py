from PyPDF2 import PdfReader, PdfWriter

def add_watermark(input_pdf, output_pdf, watermark_pdf):
    reader = PdfReader(input_pdf)
    watermark = PdfReader(watermark_pdf).pages[0]
    writer = PdfWriter()
    for page in reader.pages:
        page.merge_page(watermark)
        writer.add_page(page)
    with open(output_pdf, 'wb') as f:
        writer.write(f)
