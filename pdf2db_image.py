import cv2 as cv
import numpy as np
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (120,16)

ebl='./img_folder/test/Out1.jpg'
ROI_number=0
image = cv.imread(ebl)
original=image
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
custom_config = r'--oem 3 --psm 6'
details = pytesseract.image_to_data(gray, output_type=Output.DICT, config=custom_config, lang='eng')

total_boxes = len(details['text'])
for sequence_number in range(total_boxes):
    if int(details['conf'][sequence_number]) >30:
        (x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number],  details['height'][sequence_number])
        threshold_img = cv.rectangle(original, (x, y), (x + w, y + h), (0, 255, 0), 2)

        
plotting = plt.imshow(threshold_img)
plt.show()