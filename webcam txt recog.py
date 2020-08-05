import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

cap = cv2.VideoCapture(0)
cap.set(3, 1024)
cap.set(4, 768)
cap.set(10, 70)
while True:
    _, img = cap.read()
    hImg, wImg, _ = img.shape
    boxes = pytesseract.image_to_data(img, lang='eng')
    for x, b in enumerate(boxes.splitlines()):  # loops are counted and the count is put in x using enumerate function
        # print(b)
        if x != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.putText(img, b[11], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 255, 50), 2)
                cv2.rectangle(img, (x, y), (x + w, y + h), (50, 255, 50), 2)
                term = (b[11])
                print(term)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

