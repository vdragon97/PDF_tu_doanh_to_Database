import pdfplumber
import decimalfp

pdf = pdfplumber.open('./pdf_folder/20220523.pdf')
for page in pdf.pages:
    left = page.crop((0, 0, decimalfp.Decimal(0.5) * page.width, decimalfp.Decimal(0.9) * page.height))
    right = page.crop((decimalfp.Decimal(0.5) * page.width, 0, page.width, page.height))
    
    l_text = left.extract_text()
    r_text = right.extract_text()
    print("\n -- l_text --", l_text)
    print("\n -- r_text --", r_text)
    text = str(l_text) + " " + str(r_text)