import random
from Rectangulo import Rectangulo

# Lista con entre 10 y 1000 rectángulos de dimensiones enteras entre 1 y 10
cantidad = random.randint(10, 1000)
rectangulos = []
for i in range(cantidad):
    rectangulos.append(Rectangulo(random.randint(1, 10), random.randint(1, 10)))
print(f"Se han creado {cantidad} rectángulos\n")

# Imprimir si el objeto es un cuadrado
print("--- Cuadrados ---")
for rectangulo in rectangulos:
    if rectangulo.cuadrado:
        print(rectangulo)

# Calcular que rectángulo es el de mayor área, cual es el de mayor perímetro y cual es el de mayor lado
mayor_area = 1 # el área más baja posibles (cuadrado1*1)
for rectangulo in rectangulos:
    if rectangulo.Area() > mayor_area:
        mayor_area = rectangulo.Area()

mayor_perimetro = 4 # el perímetro más bajo posible (cuadrado 1*1)
for rectangulo in rectangulos:
    if rectangulo.Perimetro() > mayor_perimetro:
        mayor_perimetro = rectangulo.Perimetro()

mayor_lado = 1 # el lado más bajo posible (cuadrado 1*1)
for rectangulo in rectangulos:
    if rectangulo.LadoMayor() > mayor_lado:
        mayor_lado = rectangulo.LadoMayor()

# Imprimir los rectángulos de las características anteriores 
print(f"\n--- Mayor área ({mayor_area}) ---")
for rectangulo in rectangulos:
    if rectangulo.Area() == mayor_area:
        print(rectangulo)

print(f"\n--- Mayor perímetro ({mayor_perimetro}) ---")
for rectangulo in rectangulos:
    if rectangulo.Perimetro() == mayor_perimetro:
        print(rectangulo)

print(f"\n--- Lado más grande ({mayor_lado}) ---")
for rectangulo in rectangulos:
    if rectangulo.LadoMayor() == mayor_lado:
        print(rectangulo)

# Convertir en cuadrados los de mayor lado
print(f"\n--- Conversión a cuadrado de los de lado {mayor_lado} ---")
for rectangulo in rectangulos:
    if rectangulo.LadoMayor() == mayor_lado: # Comprobación que el rectágulo sea de mayor lado
        if rectangulo.cuadrado: # Comprobar si es un cuadrado (no se cambia)
            print(f"{rectangulo} -> ya era un cuadrado, no se cambia nada")
        else: # No es un cuadrado, cambiarlo
            se_cambio_base = rectangulo.ConvertirEnCuadrado() # Convertir en cuadradado
            if se_cambio_base: # Si devuelve True, se ha cambiado la base y si no la altura
                cambiado = "la base"
            else:
                cambiado = "la altura"
            print(f"Rectángulo -> Cuadrado (se cambió {cambiado})")