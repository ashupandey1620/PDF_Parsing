import fitz

pdf = fitz.open(r"C:\Users\ashup\OneDrive\Desktop\PDF Parsing\Ruskin - Immortal Stories.pdf")
print(pdf.page_count)

page = pdf.load_page(9)
text = page.gettext('text')

pdf.close()