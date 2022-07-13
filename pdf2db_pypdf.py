import pdfplumber
import pandas as pd

pdf_file = './pdf_folder/20220607.pdf'
xlsx_file = './xlsx_folder/20220607_pypdf.xlsx'

lines = []

with pdfplumber.open(pdf_file) as pdf:
    pages = pdf.pages
    for page in pdf.pages:
        '''page_text = page.extract_text(page_text = page.extract_text(layout=True,table_settings={"vertical_strategy": "text","horizontal_strategy": "text",}))'''
        page_text = page.extract_text(layout=True)
        for line in page_text.split('\n'):
            line_text = line.lstrip()
            if len(line_text) > 0 and line_text[0].isdigit():
                lines.append(line_text)
                print(line_text)
                '''
                print(line_text[0:6])
                print(line_text[6:16])
                print(line_text[16:26])
                print(line_text[26:36])
                print(line_text[36:47])
                print(line_text[47:57])
                print(line_text[57:67])
                print(line_text[67:77])
                print(line_text[77:88])
                print(line_text[88:99])
                print(line_text[99:110])
                '''
df = pd.DataFrame(lines)

#df.to_excel(xlsx_file)