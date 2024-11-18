# Reading pdf Metadata
# get total number of pdf pages
# get table of contents

import fitz
# print(fitz.__doc__)
pdf = fitz.open(r"C:\Users\ashup\OneDrive\Desktop\PDF Parsing\Ruskin - Immortal Stories.pdf")
print(pdf.page_count)
print(pdf.metadata)
print(pdf.metadata['author'])


# Table of Contents left
pdf.close()



