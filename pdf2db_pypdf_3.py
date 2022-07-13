import pdfplumber
import pandas as pd

xlsx_file = './xlsx_folder/20220523_pypdf_3.xlsx'
pdf = pdfplumber.open("./pdf_folder/20220523.pdf")

page = pdf.pages[0]

txt=page.extract_table
print(txt)


table=page.extract_table(table_settings={"vertical_strategy": "explicit",
    "horizontal_strategy": "explicit",
    "explicit_vertical_lines": page.curves+page.edges,
    "explicit_horizontal_lines": page.curves+page.edges,
    "intersection_tolerance": 15,})
format_columns = table[1]
print(format_columns)

page = pdf.pages[5]
table=page.extract_table(table_settings={"vertical_strategy": "lines", 
                                         "horizontal_strategy": "text", 
                                         "snap_tolerance": 4,
                                         "keep_blank_chars": True,})
print(f'{table}')
df = pd.DataFrame(table[1:], columns=table[0])
pd.set_option('display.max_columns', None)
df.to_excel(xlsx_file)

pdf_str = page.extract_words(use_text_flow=True)
print(pdf_str)