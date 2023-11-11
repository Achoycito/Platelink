#EASYOCR

import easyocr
reader = easyocr.Reader(['es'], gpu=True)
# output = reader.readtext('ocr_test_img/a1.png')
for i in range(10):

    print("INTENTO #",i)
    # output = reader.readtext('NA102fil.png')
    output = reader.readtext('NA102.jpeg')
    for i in output:
        print(i[1])

#pytesseract pero es kk al parecer

# import pytesseract
# import cv2

# pytesseract.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

# img_path1 = 'ocr_test_img/a2.jpg'
# text = pytesseract.image_to_string(img_path1,lang='eng')
# print(text)