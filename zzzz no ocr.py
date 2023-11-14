import cv2
import math
import os
import easyocr
import mysql.connector

def borrarCapturasEnMemoria():
    capturas = os.listdir(ruta_capturas)
    for capt in capturas:
        os.remove("cap/"+capt)

ruta_capturas = "cap"
harcascade = "model/cascade24min.xml"
matr_detectada = ""

running = True

borrarCapturasEnMemoria()

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
        borrarCapturasEnMemoria()
        running = False
        
    elif k == ord('s'):     # Si la tecla es S, se guarda la última imagen
                            # coincidencia de matrícula detectada
        try:
            if img_roi is None:
                print("No se ha detectado una matrícula todavía")
            else:
                # Codigo de que si encontro esa madre

                cv2.imwrite("cap/img"+str(count)+".jpg", img_roi)

                # reader = easyocr.Reader(["es"], gpu=True)
                # output = reader.readtext("cap/img"+str(count)+".jpg")

                # @diego
                # esta madre es la idea, no se bien como hacerle todavia pero pues no ocupas el easyocr,
                # nomas ocupas pasarle el texto que debe leer y ya
                # el de abajo no me jaló no c por que pero esa es la idea, nomas una matriz y ahi donde esta la matr poner la que quieres

                output = [[0]["CF-25-756"]] #este es el que no jalo me tira un error de int y str y quien sabe que

                for i in output:
                    if "-" in i[1]:
                        print("Numero de matricula encontrado: " + i[1])
                        print("Buscando en base de datos...")
                        matr_detectada = i[1]

                        # Esta parte no la he probado pero se supone que va a la bdd y busca la matricula
                        conexion = mysql.connector.connect(user='root', password='', host='localhost', database='platelink', port=3306)
                        cursor = conexion.cursor()
                        cursor.callproc('datosMatricula', [matr_detectada])

                        for result in cursor.stored_results():
                            resultados = result.fetchall()

                        # print("(#Matr - Año - Importada / Nombre - Paterno - Materno - CURP / #SerieVehi - Marca - Modelo - Año - Color - Ult.Revista)")

                        results_flag = False
                        for x in range(len(resultados)):
                            results_flag = True
                            print("COINCIDENCIA EN BASE DE DATOS")
                            print("Matricula: "+str(resultados[x][0]))
                            print("Año: "+str(resultados[x][1]))
                            print("Importada: "+str(resultados[x][2]))
                            print("Nombre del titular: "+str(resultados[x][3]))
                            print("Apellido paterno: "+str(resultados[x][4]))
                            print("Apellido materno: "+str(resultados[x][5]))
                            print("CURP: "+str(resultados[x][6]))
                            print("Numero de serie del vehiculo: "+str(resultados[x][7]))
                            print("Marca: "+str(resultados[x][8]))
                            print("Modelo: "+str(resultados[x][9]))
                            print("Año del vehiculo: "+str(resultados[x][10]))
                            print("Color: "+str(resultados[x][11]))
                            print("Fecha de ultima revista: "+str(resultados[x][12]))
                            # print(resultados[x])
                        if results_flag == False:
                            print("No se encontró una coincidencia en la base de datos, intente de nuevo")
                count += 1



        except NameError:
            # throw an exception or do something else
            print("No se ha detectado una matrícula todavía")
