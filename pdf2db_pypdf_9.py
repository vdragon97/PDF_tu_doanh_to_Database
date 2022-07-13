# pip install PyPDF2
# pip install pdfplumber

# ---

import pdfplumber

# ---

def scrape_sentence(phrase, lines, index):
    # -- Gather sentence 'phrase' occurs in --
    sentence = lines[index]
    print("-- sentence --", sentence)
    print("len(lines)", len(lines))
    
    # Previous lines
    pre_i, flag = index, 0
    while flag == 0:
        pre_i -= 1
        if pre_i <= 0:
            break
            
        sentence = lines[pre_i] + sentence
        
        if '.' in lines[pre_i] or '!' in lines[pre_i] or '?' in lines[pre_i] or '  •  ' in lines[pre_i]:
            flag == 1
    
    print("n", sentence)
    
    # Following lines
    post_i, flag = index, 0
    while flag == 0:
        post_i += 1
        if post_i >= len(lines):
            break
            
        sentence = sentence + lines[post_i] 
        
        if '.' in lines[post_i] or '!' in lines[post_i] or '?' in lines[post_i] or '  •  ' in lines[pre_i]:
            flag == 1 
    
    print("n", sentence)
    
    # -- Extract --
    sentence = sentence.replace('!', '.')
    sentence = sentence.replace('?', '.')
    sentence = sentence.split('.')
    sentence = [s for s in sentence if phrase in s]
    print(sentence)
    sentence = sentence[0].replace('n', '').strip()  # first occurance
    print(sentence)
    
    return sentence

# ---

phrase = '   '

with pdfplumber.open('./pdf_folder/20220607.pdf') as opened_pdf:
    for page in opened_pdf.pages:
        text = page.extract_text()
        if text == None:
            continue
        lines = text.split('n')
        i = 0
        sentence = ''
        while i < len(lines):
            if phrase in lines[i]:
                sentence = scrape_sentence(phrase, lines, i)
            i += 1
        print(text)    
