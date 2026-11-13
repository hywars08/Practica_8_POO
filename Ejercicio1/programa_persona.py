from Persona import Persona

# Primer objeto: valores elegidos por el programador
persona1 = Persona("Marco Aurelio", 10000, 821946, "hombre", 80.0, 177.0)

# Segundo objeto: todos los valores por teclado
print("--- Segunda persona ---")
nombre = input("Nombre: ")
edad = int(input("Edad: "))
dni = int(input("DNI (solo el número, sin la letra): "))
sexo = input("Sexo (hombre, mujer, no-binario): ")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (cm): "))
persona2 = Persona(nombre, edad, dni, sexo, peso, altura)

# Tercer objeto: por teclado, salvo peso, altura y sexo (fijos)
print("--- Tercera persona ---")
nombre = input("Nombre: ")
edad = int(input("Edad: "))
dni = int(input("DNI (solo el número, sin la letra): "))
persona3 = Persona(nombre, edad, dni, "mujer", 90, 185)

# Tupla con las tres personas
personas = (persona1, persona2, persona3)

# Imprimir las personas
for persona in personas:
    print(persona)
