import PyPDF2 as PyPDF
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
	merger=PyPDF.PdfFileMerger
	for pdf in pdf_list:
		print (pdf)
		merger.append(pdf)
	merger.write('merged.pdf')

pdf_combiner(inputs)