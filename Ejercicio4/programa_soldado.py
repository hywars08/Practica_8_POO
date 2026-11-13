import random
from Soldado import Soldado # Llamar a la clase "Soldado" del fichero "Soldado"

# Crear una lista vacía para meter los dos soldados (objetos)
soldados = []
# Bucle que pide los datos de cada soldado
for i in range(2):
    print(f"--- Soldado {i + 1} ---")
    nombre = input("Nombre: ")
    reino = input("Reino: ")
    vida_min = float(input("Vida mínima: "))
    vida_max = float(input("Vida máxima: "))
    # La fuerza es un valor al azar entre la vida mínima y la máxima
    fuerza = round(random.uniform(vida_min, vida_max), 2)
    soldados.append(Soldado(nombre, reino, fuerza)) # Introducir el objeto en la lista

# Mostrar el estado de los soldados antes de luchar (sus estadísticas)
print("\n=== ANTES DE LA LUCHA ===")
for soldado in soldados:
    print(soldado)

# Luchan mientras luchar() devuelva True (deja de hacerlo cuando uno muere o son del mismo reino)
peleas = 0 # Contador de peleas
# Bucle que se repite hasta que se acabe la pelea
while soldados[0].Luchar(soldados[1]):
    peleas += 1 # sumar una pelea al contador 

if peleas == 0: # Si las peleas son 0, es que no han peleado ninguna vez. La única forma para que pase eso es que sean del mismo reino o que la vida introducida al calcular la fuerza pueda acabar siendo 0.0.
    print("No han luchado: son del mismo reino o alguno está muerto.")
else:
    # Mostrar los datos de los soldados después de la pelea
    print(f"=== DESPUÉS DE LA LUCHA ({peleas} peleas) ===")
    for soldado in soldados:
        print(soldado)
