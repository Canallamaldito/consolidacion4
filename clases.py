import csv
class Vehiculo():
    def __init__(self, marca, modelo, nruedas):
        self.marca = marca
        self.modelo = modelo
        self.nruedas = nruedas
    
    def guardar_datos_csv(self):
        try:
            with open("vehiculos.csv","a", newline="") as archivo: #newline para que el archivo no quede con entre lineas en bco.
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print("No existe el archivo vehiculos.csv")
        except Exception as e:
            print("Error reportado: ", e)

    def leer_datos_csv(self):
        try:
            with open("vehiculos.csv","r") as archivo:
                #datos = [(self.__class__, self.__dict__)]
                vehiculos =csv.reader(archivo)
                print(f"\nlista de vehiculos {type(self).__name__}")
                for item in vehiculos:
                    vehiculo_tipo =str(self.__class__)
                    #print(f"lista de vehiculos {type(self).__name__}") # para el nombre de la clase
                    #print(f"lista de vehiculos {self.__class__}")  # para saber la clase 
                    #print(item) # para saber todo el cachivache
                    if vehiculo_tipo in item[0]:
                        print(item[1])
                        #print("")
        except FileNotFoundError:
            print("No existe el archivo vehiculos.csv")
        except Exception as e:
            print("Error reportado: ", e)
    
    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nruedas} ruedas "
    
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, nruedas)
        self.velocidad = velocidad 
        self.cilindraje = cilindraje
    
    def __str__(self):
        return super().__str__() + f"{self.velocidad} km/h, {self.cilindraje} cc"

class Particular(Automovil):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindraje, npasajero):
        super().__init__(marca, modelo, nruedas, velocidad, cilindraje)
        self.npasajero = npasajero
    
    def __str__(self):
        return super().__str__() + f" Puestos: {self.npasajero}"
    
    def get_npasajero(self):
        return self.npasajero
    
    def set_npasajero(self,npasajero_new):
        self.npasajero = npasajero_new
    
class Carga(Automovil):
    def __init__(self, marca, modelo, nruedas, velocidad, cilindraje, pesocarga):
        super().__init__(marca, modelo, nruedas, velocidad, cilindraje)
        self.pesocarga = pesocarga
    
    def __str__(self):
        return super().__str__() + f" Carga: {self.pesocarga} Kg"
    
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nruedas, tipobicicleta):
        super().__init__(marca, modelo, nruedas)
        self.tipobicibleta = tipobicicleta 
       
    def __str__(self):
        return super().__str__() + f"Tipo: {self.tipobicibleta}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nruedas, tipobicicleta, motor, cuadro, numradios):
        super().__init__(marca, modelo, nruedas, tipobicicleta) 
        self.cuadro = cuadro
        self.numradios = numradios
        self.motor = motor
        
    def __str__(self):
        return super().__str__() + f" Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.numradios}"
