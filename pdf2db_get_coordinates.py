from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
'''
Cloned from pdf2db_pdfminer_6
Library pdfminer
Only handle page with header
'''
def __main__(pdf_file ):
    fp = open(pdf_file, 'rb')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)
    columns_list = []
    i = -1
    correction = 16
    
    for page in pages:
        columns = []
        i = i + 1
        #print('Processing next page...')
        interpreter.process_page(page)
        layout = device.get_result()
        for lobj in layout:
            if isinstance(lobj, LTTextBox):
                x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                #print('At %r is text: %s' % ((x, y), text))
                if text.find("Mua") != -1:
                    #print('At %r is text: [%s]' % ((x, y), text))
                    columns.append(x - correction)
                if text.find("Bán") != -1:
                    #print('At %r is text: [%s]' % ((x, y), text))
                    columns.append(x - correction)
                if (text.find("Tổng cộng") != -1) or (text.find("-->") != -1):
                    #print('At %r is text: [%s]' % ((x, y), text))
                    columns.insert(0, x + correction)
        columns.insert(0, i)
        
        columns_list.append(columns)
    return columns_list
    
'''
[[0, 73.88, 158.34, 232.98, 305.01, 379.65, 451.67, 526.31, 598.34, 673.0] ->header page
[1] -> normal page
[2]
[3, 90.92, 187.02, 254.7, 326.85, 396.57, 454.31, 514.91, 578.78, 651.02] 
[4]
[5]]
'''    