import csv

class Vehiculo:
    def __init__(self, marca, modelo, ruedas):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = ruedas
        
        
    def __str__(self):
        return(f"Marca {self.marca}, Modelo {self.modelo}, {self.ruedas} ruedas")
    
    def crear_vehiculo_csv():
        try:
            with open ("vehiculos.csv", "w"):
                print("Archivo borrado y creado de forma exitosa")
        except Exception as error:
            print("Error inesperado:", error)
    def guardar_datos_csv(self):

        try:
            with open ("vehiculos.csv", "a", newline="") as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivoCsv= csv.writer(archivo)
                archivoCsv.writerows(datos)
        except FileNotFoundError:
            print("Archivo no encontrado, por favor cree el archivo antes de agregar información.")
        except Exception as error:
            print("Error inesperado: ", error)


    def leer_datos_csv():
        try:
            with open("vehiculos.csv", "r") as archivo:
                cont = csv.reader(archivo)
                for item in cont:                
                    for elm in item:
                        if item.index(elm)%2 == 0:
                            print("\nLista de Vehiculos ", (elm.split(".")[1][:-2]))
                        elif item.index(elm)%2 != 0:
                            print(elm)
        except FileNotFoundError:
            print("Archivo no encontrado, por favor cree el archivo antes de leerlo")
        except Exception as error:
            print("Error inesperado: ", error)

                
                  
        
                        

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    
    def __str__(self):
        return super().__str__() + f", {self.velocidad} km/h, {self.cilindrada} cc"

class Particular(Automovil):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindrada, puestos):
        super().__init__(marca, modelo, ruedas, velocidad, cilindrada)
        self.puestos = puestos
        
# ----Getters y setters para Particular---
    def get_puestos(self):
        return self.puestos
    
    def set_puestos(self, setPuestos):
        self.puestos = setPuestos
#-------------------------------------------
    def __str__(self):
        return super().__str__() + f", Puestos: {self.get_puestos()}"
    
class Carga(Automovil):
    def __init__(self, marca, modelo, ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, ruedas, velocidad, cilindrada)
        self.carga = carga
        
    
    def __str__(self):
        return super().__str__() + f", Carga: {self.carga} Kg"
    
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, ruedas, tipo):
        super().__init__(marca, modelo, ruedas)
        self.tipo = tipo
        
    
    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}"
    
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, ruedas, tipo, radios, cuadro, motor):
        super().__init__(marca, modelo, ruedas, tipo)
        self.radios = radios
        self.cuadro = cuadro
        self.motor = motor
        
    def __str__(self):
        return super().__str__() + f", Motor: {self.motor}T, Cuadro: {self.cuadro} Radios: {self.radios}"
    
