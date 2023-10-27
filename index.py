import mysql.connector

conexion = mysql.connector.connect(user='root', password='', host='localhost', database='platelink', port=3306)

cursor = conexion.cursor()

while(True):
    matricula = input("Escribe el numero de matricula separado con guiones: ")

    cursor.callproc('datosMatricula', [matricula])

    #653-PNK-1
    #388-PNK-7
    #877-PNL-1
    #217-PNE-9
    #521-PNJ-8

    for result in cursor.stored_results():
        resultados = result.fetchall()

    print("(#Matr - Año - Importada / Nombre - Paterno - Materno - CURP / #SerieVehi - Marca - Modelo - Año - Color - Ult.Revista)")
    for x in range(len(resultados)):
        print(resultados[x])
    print("")
