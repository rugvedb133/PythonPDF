import PyPDF2
import sys

file = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))
watermark = PyPDF2.PdfFileReader(open(sys.argv[2], 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('watermarked_output.pdf', 'wb') as out_file:
    output.write(out_file)
