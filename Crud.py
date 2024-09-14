#Crud: create, read, update and delete

import time
import os
import mysql.connector

#Crearemos la conexión a la DB

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "prueba1"
)

mycursor = mydb.cursor()

while True:
    print("****MENU DEL SISTEMA****"
          "\n 1. Insertar un dato."
          "\n 2. Eliminar un dato."
          "\n 3. Buscar un dato."
          "\n 4. Sobreescribir un dato"
          "\n 5. Mostrar el contenido de la tabla"
          "\n 6. Salir del sistema.")
    opcion = int(input("Elige una opción: "))
    if opcion ==1:
        dato = input("Ingresa el dato a insertar: ")
        sql = "INSERT INTO datos (dato) VALUES (%s)"
        val = (dato,)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "Registros intertados.")
        time.sleep(2)
        os.system('cls')
    elif opcion == 2:
        dato = input("Ingresa el dato a eliminar: ")
        sql = "DELETE FROM datos WHERE dato = %s)"
        val = (dato,)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "Registros eliminados.")
        time.sleep(2)
        os.system('cls') #clear screen
    elif opcion == 3:
        dato = input("Ingresa el dato a buscar: ")
        sql = "SELECT * FROM datos WHERE dato = %s)"
        val = (dato,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        if myresult:
            print("El dato está en la tabla")
        else:
            print("El dato no existe en la tabla")
        time.sleep(2)
        os.system('cls') #clear screen
    elif opcion == 4:
        dato_anterior = input("Ingresa el producto a reemplazar/actualizar: ")
        dato_nuevo = input("Ingresa el nuevo producto: ")
        sql = "UPDATE datos SET datos = %s WHERE dato = %s)"
        val = (dato_nuevo, dato_anterior)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "Registros actualizados.")
        time.sleep(2)
        os.system('cls') #clear screen
    elif opcion == 5:
        mycursor.execute("SELECT * FROM datos")
        myresult = mycursor.fetchall()
        print("Estás visualizando los productos en general")
        for x in myresult:
            print(x)
        time.sleep(5)
        os.system('cls') #clear screen
    elif opcion = 6:
        respuesta = input ("Estás seguro de salir?: (s/n) ")
        if respuesta.upper() == "S":
            print("Saliendo del sistema")
            time.sleep(2)
            os.system('cls')
            break
    else:
        print("Opción no válida, intenta de nuevo...")
        time.sleep(2)
        os.system('cls')

mydb.close()


#cd \xampp\mysql\bin
#mysql -u root -h localhost -p
#create database pruebaperu;
#use pruebaperu;

#code con error debido al cmd no coge la ejecución
