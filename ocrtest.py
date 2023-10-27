import easyocr

reader = easyocr.Reader(['es'])

# output = reader.readtext('plate.jpg')
output = reader.readtext('ocr_test_img/a7.jpeg')

for i in output:
    print(i[1])