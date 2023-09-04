# Digital Ground

import pdf2docx
from pdf2docx import Converter

pdf_file = 'demo.pdf'
docx_file = 'demo.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()




