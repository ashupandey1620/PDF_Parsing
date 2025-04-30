from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_path, output_folder):
    reader = PdfReader(input_path)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        with open(f"{output_folder}/page_{i+1}.pdf", 'wb') as f:
            writer.write(f)
