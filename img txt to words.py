import cv2
import pytesseract
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('TEXT.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# [   0          1           2           3           4          5         6       7       8        9        10       11 ]
# ['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text']
boxes = pytesseract.image_to_data(img)
for x, b in enumerate(boxes.splitlines()): #loops are counted and the count is put in x using enumerate function
    #print(b)
    if x != 0:
        b = b.split()
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.putText(img, b[11], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
            cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 255), 2)
            translator = Translator()
            sentence = " "
            sentence = sentence + " " + b[11]
            print(sentence)
            a = translator.translate(sentence, dest='ta')
            print(a)

cv2.imshow('img', img)
cv2.waitKey(0)