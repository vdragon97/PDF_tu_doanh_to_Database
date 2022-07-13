import camelot
from camelot.io import read_pdf
import pandas
from matplotlib import pyplot as plt
tables = camelot.read_pdf('./pdf_folder/20220607.pdf', pages='all', flavor='stream', suppress_stdout=True,)
camelot.plot(tables[0], kind='text')
plt.show()
camelot.plot(tables[0], kind='grid')
plt.show()
print(tables[5].df)
#tables
tables.export('./xlsx_folder/20220607_camelot.csv', f='csv', compress=False)
#tables.export('./xlsx_folder/20220523_camelot.html', f='html', compress=True)
'''
tables[0]
tables[0].parsing_report
'''
'''
tables[0].to_sqlite('./xlsx_folder/20220523_camelot.sql')

for table in tables:
    table_df = table.df
    table.parsing_report
'''