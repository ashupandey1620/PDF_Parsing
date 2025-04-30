import fitz  # PyMuPDF

def extract_images_from_pdf(pdf_path, output_folder):
    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            with open(f"{output_folder}/image{i}_{xref}.png", "wb") as f:
                f.write(base_image["image"])
