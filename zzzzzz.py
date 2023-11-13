import cv2
import math
import os
import easyocr
import mysql.connector

ruta_capturas = "C:\\Users\\Alan Gonzalez\\Documents\\Platelink\\cap"
harcascade = "model/cascade24min.xml"
matr_detectada = ""

running = True

cap = cv2.VideoCapture(0)

cap.set(3, 640) #Ancho
cap.set(4, 480) #Alto

min_area = 10000 #Area minima de la imagen de la matricula
count = 0

while running:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade) #Detectar con el haar
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Colorear imagen en escala de grises

    plates = plate_cascade.detectMultiScale(img, 1.1, 4)

    for(x, y, w, h) in plates:
        wco = math.floor(w*0.1)
        hco = math.floor(h*0.1)

        area = (w + wco*2) * (h+ hco*2)

        if area > min_area: #Creo que aquí está checando que lo que detectó sea de un tamaño minimo para ver si se trata de una placa o nel
            # cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 255), 2) #Crea un rectangulo en la imagen que capturo de la matricula (x, y, ancho, alto, color, grosor)
            cv2.rectangle(img, (x-hco,y-hco), (x+w+wco, y+h+hco), (0, 255, 0), 2) #Crea un rectangulo en la imagen que capturo de la matricula (x, y, ancho, alto, color, grosor)
            cv2.putText(img, "MATRICULA", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2) #Escribir texto "Num Placa" (pos, fuente, tamaño, color, grosor)

            yCoord = y-hco if y-hco>0 else y
            xCoord = x-wco if x-wco>0 else x

            #Ventanita con el puro resultado
            img_roi = img[yCoord: y+h+hco, xCoord:x+w+wco]
            cv2.imshow("Extracted", img_roi)

    cv2.imshow("Result", img) #Ventanita

    #Se presiona una tecla
    k = cv2.waitKey(1)

    if k == ord('q'):       # Si la tecla es Q se borran todas
                            # las imágenes y se cierra el programa
        capturas = os.listdir(ruta_capturas)
        for capt in capturas:
            os.remove("cap/"+capt)
        running = False
        
    elif k == ord('s'):     # Si la tecla es S, se guarda la última imagen
                            # coincidencia de matrícula detectada
        cv2.imwrite("cap/img"+str(count)+".jpg", img_roi)

        reader = easyocr.Reader(["es"], gpu=True)
        output = reader.readtext("cap/img"+str(count)+".jpg")

        for i in output:
            if "-" in i[1]:
                print("Numero de matricula encontrado: " + i[1])
                matr_detectada = i[1]

                # Esta parte no la he probado pero se supone que va a la bdd y busca la matricula
                # conexion = mysql.connector.connect(user='root', password='', host='localhost', database='platelink', port=3306)
                # cursor = conexion.cursor()
                # cursor.callproc('datosMatricula', ["CF-25-756"])

                # for result in cursor.stored_results():
                #     resultados = result.fetchall()

                # print("(#Matr - Año - Importada / Nombre - Paterno - Materno - CURP / #SerieVehi - Marca - Modelo - Año - Color - Ult.Revista)")
                # for x in range(len(resultados)):
                #     print(resultados[x])
        count += 1

