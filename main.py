#importación de archivos

from vehiculos import *


#objetos a ocupar en el programa, tanto en la parte 2 como en la 3:

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

#Menú y programa
validador = True

while validador:
    y = input("""
    \033[01m\033[34mExamen Modulo 4, Darío Prado

    Por favor seleccione la sección de la prueba que desea ejecutar
    escriba 1, 2 o 3; escriba 0 para salir del programa:\033[0m
    """)

    if y =="1":
        listado = []

        num = int(input("Escriba cuantos vehiculos desea insertar: "))
        i = 0
        while i<num:
            print(f"\nDatos del automovil {i+1}")
            marca = input("inserte la marca del automovil: ")
            modelo = input("inserte el modelo: ")
            ruedas = input("Inserte el número de ruedas: ")
            velocidad = input("Inserte la velocidad en km/h: ")
            cilindraje = input("Inserte el cilindraje en cc: ")
            automovil = Automovil(marca,modelo,ruedas,velocidad, cilindraje)
            listado += [automovil]
            i+=1

        for item in listado:
            print (f"\nDatos del automovil {listado.index(item)+1} : {item}")

    if y =="2":

        print("")
        print(particular)
        print(carga)
        print(bicicleta)
        print(motocicleta)

        print(f"""
        Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}
        Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}
        Motocicleta es instancia con relación a Vehículo Particular: {isinstance(motocicleta, Particular)}
        Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}
        Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}
        Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}
        """)

    if y == "3":
        while validador:
            z= input("""\033[01m\033[36m
Seleccione que desea hacer:
-Escriba 1 para crear y/o escribir los datos requeridos en el archivo vehiculos.csv.
-Escriba 2 para leer los datos contenidos en vehiculos.csv
-Escriba 0 para salir del programa.

Ingrese su selección: \033[0m
""")

            if z == "1":
                particular.guardar_datos_csv()
                carga.guardar_datos_csv()
                bicicleta.guardar_datos_csv()
                motocicleta.guardar_datos_csv()
                print("El archivo vehiculos.csv ha sido creado y/o escrito exitosamente")

            elif z =="2":
                Vehiculo.leer_datos_csv()

            
            elif z =="0":
                print("\033[01m\033[31mSaliendo del programa, ¡Adios!\033[0m")
                validador = False
            else:
                print("Selección incorrecta intente nuevamente")

    if y =="0":
        print("\033[01m\033[31mSaliendo del programa, ¡Adios!\033[0m")
        validador = False
    
    else:
        print("Selección incorrecta intente nuevamente")