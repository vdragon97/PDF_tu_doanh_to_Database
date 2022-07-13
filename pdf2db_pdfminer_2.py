#jpg_file = 'C:/Users/LONG.PV/Desktop/PDF_tu_doanh_to_Database/img_folder/test/Out1.jpg'     
pdf_file = './pdf_folder/20220523.pdf'  



import io
import os
import IPython
from pdfminer3.converter import TextConverter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfpage import PDFPage
import pandas as pd # possibly necessary to convert into csv
import csv
 
# Setting up the pdf file for processing and extracting the text in it into a string
 
resource_manager = PDFResourceManager()
out_text = io.StringIO()
converter = TextConverter(resource_manager, out_text, laparams=LAParams())
page_interpreter = PDFPageInterpreter(resource_manager, converter)
 
def searchpdf():
    pathextension = r'./pdf_folder'  # -----> Folder where all the files are stored
    for path in os.listdir(pathextension):
        full_path = os.path.join(pathextension, path)
        # Checks the folder and then the extension of the file
        if os.path.isfile(full_path) and os.path.splitext(path)[1] == ".pdf":
            # Opens each path and associated pdf file
            with open(full_path, 'rb') as searchfullpdf:
                # Running scans over each file
                for page in PDFPage.get_pages(searchfullpdf, caching=True, check_extractable=True):
                    page_interpreter.process_page(page)
                     
    textfound = out_text.getvalue()  # Returns the values found in each file
    return textfound
    
    
if __name__ == '__main__':    
    outputText = searchpdf().split('\n')
    print(outputText)
    
    writer=csv.writer(open("file.csv","w"))
    writer.writerow(outputText)