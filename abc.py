import pdfplumber
import numpy as np

pdf_file = './pdf_folder/20220607.pdf'
tables = []
'''
with pdfplumber.open(pdf_file) as pdf:
    pages = pdf.pages
    for each_page in pdf.pages:
        page_table = each_page.extract_table(table_settings={"vertical_strategy": "lines", 
                                         "horizontal_strategy": "text", 
                                         "snap_tolerance": 4,})
        tables.extend(page_table)                                 
'''
pdf = pdfplumber.open(pdf_file)
page = pdf.pages[4]
page_table = page.extract_table(table_settings={"vertical_strategy": "text", 
                                         "horizontal_strategy": "text", 
                                         "snap_tolerance": 4,})
tables.extend(page_table)                                         
#print(tables)

tables_2 = []
for each_row in range(len(tables)):
    print(tables[each_row])
    #filter header row
    if 'Stt' in tables[each_row][0] or '-->' in tables[each_row][0]:
        continue
    #filter index column        
    if tables[each_row][0].isdigit(): 
        tables[each_row].pop(0)
        #resize to 9 elements
        for n in range(len(tables[each_row]), 9):
            tables[each_row].append('0')
        #print (tables[each_row])
        
        #fix elements
        
        
        tables_2.append(tables[each_row])
        continue
    #normal row    
    if len(tables[each_row][0]) >= 3:
        #resize to 9 elements
        for n in range(len(tables[each_row]), 9):
            tables[each_row].append('0')
        #fix elements
    
        #print (tables[each_row])
        tables_2.append(tables[each_row])
#print(tables_2)

#fix cell
tables_3 = []
for each_row in range(len(tables_2)):
    tables_3.append([i.replace(',', '') for i in tables_2[each_row]])
    #print(tables_3[each_row])
#print(tables_3)

tables_4 = []
for each_row in range(len(tables_3)):
    tables_4.append([0 if i == '' else i for i in tables_3[each_row]])
    #print(tables_4[each_row])
    
#def __main__():