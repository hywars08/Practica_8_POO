from IntervaloTemporal import IntervaloTemporal

cantidad = int(input("¿Cuántos intervalos temporales quieres? "))
intervalos = []

# Bucle que se repite la cantidad de veces igual al número de intervalos pedidos
while len(intervalos) < cantidad:
    print(f"--- Intervalo {len(intervalos) + 1} de {cantidad} ---")
    hora_inicio = int(input("Hora inicial: "))
    minuto_inicio = int(input("Minuto inicial: "))
    hora_fin = int(input("Hora final: "))
    minuto_fin = int(input("Minuto final: "))
    intervalo_nuevo = IntervaloTemporal(hora_inicio, minuto_inicio, hora_fin, minuto_fin)

    # Comprobacion si el intervalo introducido ya ha sido introducido o no
    if intervalo_nuevo in intervalos:  
        print("Ese intervalo ya existe, introduce uno nuevo.")
    else:
        # Se inserta antes del primer intervalo más largo: los más cortos primero
        posicion = 0
        while posicion < len(intervalos) and not intervalo_nuevo < intervalos[posicion]: # Se va a ir avanzando posicion siempre y cuando este dentro de los huecos de la lista y el intervalo nuevo sea mayor que el que esta en esa posicion
            posicion += 1
        intervalos.insert(posicion, intervalo_nuevo) # Es como el append pero permite especificar la posicion en la lista

# Imprimir el intervalo temporal y a que intervalo pertenece del día
for intervalo in intervalos:
    print(intervalo)
