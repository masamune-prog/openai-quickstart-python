from PyPDF2 import PdfFileReader
#from the pdf or webpage, get the original 

import pikepdf

#Open PDF with pikepdf
pdf = pikepdf.Pdf.open('D:\openai-quickstart-python\s12915-022-01347-7.pdf')

#Extract metadata from PDF
pdf_info = pdf.docinfo

#Print out the metadata
for key, value in pdf_info.items():
    print(key, ':', value)

