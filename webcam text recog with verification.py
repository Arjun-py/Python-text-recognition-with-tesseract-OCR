import cv2
import pytesseract
import PyDictionary as PD

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

cap = cv2.VideoCapture(0)
cap.set(3, 1024)
cap.set(4, 768)
cap.set(10, 60)

while True:
    _, img = cap.read()
    hImg, wImg, _ = img.shape
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Convert image to black and white (using adaptive threshold)
    # adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
    # DETECTING CHARACTERS
    boxes = pytesseract.image_to_data(img)
    for x, b in enumerate(boxes.splitlines()):  # loops are counted and the count is put in x using enumerate function
        # print(b)
        if x != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.putText(img, b[11], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 255, 50), 2)
                cv2.rectangle(img, (x, y), (x + w, y + h), (50, 255, 50), 2)
                term = (b[11])
                term = term.lower()
                lst = list()
                lt = list()
                lst.append(term)
                for term in lst:
                    c = PD.PyDictionary.meaning(term=term)
                    for word in str(c):
                        if word == "Error:":
                            # print(term)
                            cv2.imshow("Result", img)
                            continue
                        else:
                            cv2.imshow("Result", img)
                            print(term)
                            lt.append(term)
                            print(lt)
                            break
                    #print(lt)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
