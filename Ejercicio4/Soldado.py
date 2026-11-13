# D=================================================================================================================== #
# Título: Ejercicio 4.	
# Crea una clase Soldado con las siguientes características:
# Atributos:
# ●	nombre: str.  Se deberá validar que es una cadena con al menos 1 carácter.
# ●	reino: str.   Se deberá validar que es una cadena con al menos 1 carácter.
# ●	fuerza float. Se deberá validar que es un número positivo.
# ●	batallas: int. Guarda el número de batallas del soldado. Se deberá validar que es un número entero positivo.
# 	 Métodos especiales:
# ●	init:  recibirá el nombre del soldado, el reino al que pertenece y su fuerza. Establecerá a 0 el número de batallas 
#   del soldado.
# ●	eq: Comparará si la fuerza de los dos soldados es igual.
# ●	gt: Comparará si la fuerz del soldado es mayor que el del otro soldado.
# ●	str: Devuelve un String para imprimir los datos del soldado por pantalla siguiendo el siguiente formato:
# Información soldado:
# Nombre: Pepe
# Reino: Aragón
# Batallas: 4
# Estado: Vivo
# Fuerza: 34.00 ptos
# 	Otros métodos:
# ●	luchar(soldado: Soldado) -> bool: Método que refleja la lucha entre dos soldados vivos de distinto reino. 
#   Gana el soldado con mayor ataque. Cada soldado pierde un tercio de la fuerza del otro soldado. 
#   Ambos soldados incrementan el número de batallas en 1. Devuelve si han luchado.
# Crear un programa que solicite al usuario todos los datos necesarios para crear 2 soldados. 
# Para calcular su fuerza, habrá que pedir la vida min y la vida max. Imprime la información de cada soldado. 
# Haz que luchen entre ellos hasta que uno muera e imprime la información de cada soldado después de la lucha.
# Autor: Miguel Jun Patricio Ferrer
# Fecha: 10/11/26
# Version: 1.0
# D=================================================================================================================== #

# C=================================================================================================================== #
# Nombre de la clase: Soldado
# Descripción: Gestiona datos de un soldado (nombre, reino, fuerza) y luego contiene diversos métodos. 
# El más importante el que realiza las peleas entre dos soldados
# Autor: Miguel Jun Patricio Ferrer
# Fecha de creación: 10/11/26
# Fecha de ult. modificación: 10/11/26
# Anotaciones extra:
# C=================================================================================================================== #

import random

class Soldado:
    def __init__(self, nombre: str, reino: str, fuerza: float):
        self.nombre = nombre
        self.reino = reino
        self.fuerza = fuerza
        self.batallas = 0

    # --- PROPIEDADES ---
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        if type(nombre) != str:
            raise TypeError("El nombre debe ser texto")
        elif len(nombre) < 1:
            raise ValueError("El nombre debe tener al menos un carácter")
        else:
            self.__nombre = nombre

    @property
    def reino(self):
        return self.__reino

    @reino.setter
    def reino(self, reino: str):
        if type(reino) != str:
            raise TypeError("El reino debe ser texto")
        elif len(reino) < 1:
            raise ValueError("El reino debe tener al menos un carácter")
        else:
            self.__reino = reino

    @property
    def fuerza(self):
        return self.__fuerza

    @fuerza.setter
    def fuerza(self, fuerza: float):
        if type(fuerza) != int and type(fuerza) != float:
            raise TypeError("La fuerza debe ser un número")
        elif fuerza < 0:  # 0 se permite: es la fuerza de un soldado muerto
            raise ValueError("La fuerza no puede ser negativa")
        else:
            self.__fuerza = float(fuerza)

    @property
    def batallas(self):
        return self.__batallas

    @batallas.setter
    def batallas(self, batallas: int):
        if type(batallas) != int:
            raise TypeError("Las batallas deben ser un número entero")
        elif batallas < 0:
            raise ValueError("Las batallas no pueden ser negativas")
        else:
            self.__batallas = batallas

    # --- MÉTODOS ---
    # Sirve para comprobar si un soldado esta vivo
    def EstaVivo(self): 
        return self.fuerza > 0.0

    def __eq__(self, otro):
        return self.fuerza == otro.fuerza

    def __gt__(self, otro):
        return self.fuerza > otro.fuerza

    def __str__(self):
        # Comprobación si esta vivo o no el soldado
        if self.EstaVivo():
            estado = "Vivo"
        else:
            estado = "Muerto"
        return (f"Información soldado:\n"
                f"Nombre: {self.nombre}\n"
                f"Reino: {self.reino}\n"
                f"Batallas: {self.batallas}\n"
                f"Estado: {estado}\n"
                f"Fuerza: {self.fuerza:.2f} ptos")

    # Simula la lucha de dos soldados
    def Luchar(self, soldado):
        # Si alguno de los dos solados esta muerto o son del mismo reino devolver False
        if (not self.EstaVivo() or not soldado.EstaVivo()) or (self.reino.lower() == soldado.reino.lower()):
            han_luchado = False
        else:
            han_luchado = True
            if self == soldado:  # Empate: se decide al azar quién pierde
                if random.randint(0, 1) == 0:
                    self.fuerza = max(0.0, self.fuerza - soldado.fuerza / 3) # Se utiliza la función más para que la fuerza nunca baje de 0
                else:
                    soldado.fuerza = max(0.0, soldado.fuerza - self.fuerza / 3) # Se utiliza la función más para que la fuerza nunca baje de 0
            elif self > soldado:  # Gana el soldado 1 pierde el 2
                soldado.fuerza = max(0.0, soldado.fuerza - self.fuerza / 3) # Se utiliza la función más para que la fuerza nunca baje de 0
            else:  # Gana el soldado 2 pierde el 1
                self.fuerza = max(0.0, self.fuerza - soldado.fuerza / 3) # Se utiliza la función más para que la fuerza nunca baje de 0

        # Sumar al contador de las batallas de cada soldado
        self.batallas += 1
        soldado.batallas += 1
        return han_luchado