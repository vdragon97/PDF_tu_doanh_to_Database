import tabula
import pandas as pd
import numpy as np
import pprint
    
def __main__(pdf_file, page, cols):
    tables = tabula.read_pdf(pdf_file, pages = page, stream=True, guess=False, pandas_options={'header': None},
            columns=cols)
    #print( tables)
    
    tables_2 = []
    tables_2 = np.array(tables).tolist()
    
    tables_3 = []
    tables_3 = tables_2[0]
    #print(len(tables_3))
    
    tables_4 = []
    for each_row in range(len(tables_3)):
        
        tables_3[each_row].pop(0)
        for n in range(len(tables_3[each_row]), 9):
            tables_3[each_row].append('0')
        tables_4.append(tables_3[each_row])    
    #print(tables_4)       
    return tables_4
    #fix cell
    '''
    tables_5 = []
    
    t_5 = []
    for each_row in range(len(tables_4)):
        for i in range(len(tables_4[each_row])):
            #print(str(tables_4[each_row][i]).replace('nan', '0').replace(',', ''))
            t_5.append(str(tables_4[each_row][i]).replace('nan', '0').replace(',', ''))
        #print(t_5)
        tables_5 = np.array(t_5)    
        #t_5.clear()
    #print(tables_5) #<class 'numpy.ndarray'>
    
    '''