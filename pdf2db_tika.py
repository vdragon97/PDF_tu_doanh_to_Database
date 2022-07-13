import requests
import io
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTText, LTChar, LTAnno, LTTextBoxHorizontal, LTTextBox, LTTextLine
def parse_char_layout(layout):

# bbox:
# x0： The distance from the left side of the page to the left edge of the box .
# y0： The distance from the bottom of the page to the bottom edge of the box .
# x1： The distance from the left side of the page to the right edge of the box .
# y1： The distance from the bottom of the page to the top edge of the box 
    for textbox in layout:
        if isinstance(textbox, LTText):
            for line in textbox:
                for char in line:
                    # If the char is a line-break or an empty space, the word is complete
                    if isinstance(char, LTAnno) :
                        pass
                    elif char.get_text() == ' ':
                        print(" coordinate x:", char.bbox[0], "y:", char.bbox[3], " ||| ", "NaN")
                    elif isinstance(char, LTChar):
                        print(" coordinate x:", char.bbox[0], "y:", char.bbox[3], " ||| ", char.get_text())
def parse_char_layout_2(layout):     
    for lobj in layout:
        if isinstance(lobj, LTTextBoxHorizontal):
            x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
            print('At %r is text: %s' % ((x, y), text))       
def parse_char_layout_3(layout):     
    for lt_obj in layout:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            print( lt_obj.get_text() )
            
if __name__ == '__main__':
    #req = requests.get('./pdf_folder/20220523.pdf')
    #fp = io.BytesIO(req.content)
    fp = open('./pdf_folder/20220523.pdf', 'rb')
    parser = PDFParser(fp) # Create a file object pdf Document analyzer 
    doc: PDFDocument = PDFDocument(parser) # establish pdf file 
    rsrcmgr = PDFResourceManager() # establish PDF, Explorer , To share resources 
    # Create a PDF Device objects 
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    # Create a PDF Explain its object 
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Loop through the list , Deal with one at a time page Content 
    # doc.get_pages() obtain page list 
    
    #interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process the contents of each page in the document object 
    # doc.get_pages() obtain page list 
    # Loop through the list , Deal with one at a time page The content of 
    # here layout It's a LTPage object There is... In it This page All kinds of objects analyzed Generally include LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal wait If you want to get the text, get the name of the object text attribute ,
    for page in PDFPage.create_pages(doc):
        print('================ New page ================')
        interpreter.process_page(page)
        layout = device.get_result()
        #parse_char_layout(layout) # Analytic alphabet 
        #parse_char_layout_2(layout)
        parse_char_layout_3(layout)
