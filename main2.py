from clases import Vehiculo, Automovil, Particular, Carga, Bicicleta, Motocicleta

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print("")
print(particular)
print(carga)
print(bicicleta)
print(motocicleta)
print("")

print("Motocicleta es instancia con relación a Vehículo: ", isinstance(motocicleta, Vehiculo)) 
print("Motocicleta es instancia con relación a Automovil: ", isinstance(motocicleta, Automovil)) 
print("Motocicleta es instancia con relación a Vehículo particular: ", isinstance(motocicleta, Particular)) 
print("Motocicleta es instancia con relación a Vehículo de Carga: ", isinstance(motocicleta, Carga)) 
print("Motocicleta es instancia con relación a Bicicleta: ", isinstance(motocicleta, Bicicleta)) 
print("Motocicleta es instancia con relación a Motocicleta: ", isinstance(motocicleta, Motocicleta)) 
print("")



