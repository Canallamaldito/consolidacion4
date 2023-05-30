from clases import Vehiculo, Automovil

instancias = []
# ingeso de instancias manual

n = int(input("cuantos Vehiculos desesa insertar: "))
for i in range(n):
    print(f"Datos del Automóvil {i+1}")
    marca = input("Inserte la marca del Automóvil: ")
    modelo = input("Inserte el modelo: ")
    nruedas = int(input("Inserte el numero de ruedas "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindraje = int(input("inserte el cilindraje en cc: "))
    print("")
    auto = Automovil(marca, modelo, nruedas, velocidad, cilindraje)
    instancias.append(auto)

### AUTO LLENADO PARA NO LLENAR A CADA RATO
"""
auto = Automovil("Toyota", "Yaris", 4, 120, 800)
instancias.append(auto)
auto = Automovil("Fiat", "Palio", 4, 95, 1200)
instancias.append(auto)
auto = Automovil("Ford", "Fiesta", 4, 125, 1500)
instancias.append(auto)
"""
print("Imprimiendo por pantalla los vehiculos: ")

for index, item in enumerate(instancias):
        print(f"Datos del automovil {index+1} : marca {item.marca}, Modelo {item.modelo}, {item.nruedas} ruedas, {item.velocidad} km/h,{item.cilindraje} cc")
    