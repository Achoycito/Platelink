import cv2

#harcascade = "model/haarcascade_russian_plate_number.xml"

# harcascade = "model/bcs_plate_cascade.xml"
# harcascade = "model/bcs_cascade_2.xml"
harcascade = "model/cascade.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640) #Ancho
cap.set(4, 480) #Alto

min_area = 10000 #Area minima de la imagen de la matricula

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade) #Detectar con el haar
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Colorear imagen en escala de grises

    plates = plate_cascade.detectMultiScale(img_grey, 1.1, 4)

    for(x, y, w, h) in plates:
        area = w*h

        if area > min_area: #Creo que aquí está checando que lo que detectó sea de un tamaño minimo para ver si se trata de una placa o nel
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2) #Crea un rectangulo en la imagen que capturo de la matricula (x, y, ancho, alto, color, grosor)
            cv2.putText(img, "MATRICULA", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2) #Escribir texto "Num Placa" (pos, fuente, tamaño, color, grosor)

            #Ventanita con el puro resultado
            img_roi = img[y: y+h, x:x+w]


    cv2.imshow("Result", img) #Ventanita

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
