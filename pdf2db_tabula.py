import tabula
import pandas as pd

pdf_file = './pdf_folder/20220523.pdf'
#tables = tabula.read_pdf('./pdf_folder/20220523.pdf', pages = '6', stream=True, guess=False, pandas_options={'header': None})
tables = tabula.read_pdf('./pdf_folder/20220523.pdf', pages = '6', stream=True, guess=False, pandas_options={'header': None},
        columns=( 90.96,186.62,254.66,328.25,396.53,468.31,517.39,592.78,650.98,))

'''tabula.convert_into(".\pdffile\IPLmatch.pdf", "iplmatch.csv", output_format="csv", pages='all')
'''
print(tables)
result_df = pd.concat(tables)
result_df.to_excel('./xlsx_folder/20220523_tabular.xlsx')