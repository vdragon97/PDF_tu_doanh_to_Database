import pdfplumber

pdf = './pdf_folder/20220523.pdf'

with pdfplumber.open(pdf) as pdf:
    '''pages = pdf.pages
    for page in pdf.pages:
    '''
    page_count = len(pdf.pages)
    print(page_count)
    i = 0
    while i < page_count:
        page = pdf.pages[i]
        line_pos = max(r["bottom"] for r in page.rects)
        table = page.extract_table({
            "explicit_horizontal_lines": [ line_pos ]
        })
        
        im = page.to_image(resolution=300)
        line_pos = max(r["bottom"] for r in page.rects)
        im.reset().debug_tablefinder({
            "explicit_horizontal_lines": [ line_pos ]
        }).save('Out' + str(i) + '.jpg')
        i += 1
        
        