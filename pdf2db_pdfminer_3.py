PDFfilename = './pdf_folder/20220523.pdf'  

import PyPDF2
 
 
pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb")) #PdfFileReader object

pg3 = pfr.getPage(2) #extract pg 2
writer = PyPDF2.PdfFileWriter() #create PdfFileWriter object
 
#add pages
writer.addPage(pg3)
 
#filename of your PDF/directory where you want your new PDF to be
NewPDFfilename = "abc.txt" 
 
with open(NewPDFfilename, "wb") as outputStream: #create new PDF
    writer.write(outputStream) #write pages to new PDF