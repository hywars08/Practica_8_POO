# D=================================================================================================================== #
# Título: Ejercicio 1.	
# Crear una clase Persona que contenga los siguientes atributos: nombre, edad, DNI, letraDNI, sexo 
# (hombre, mujer, no-binario), peso y altura. Crear un método init dando valor adecuado a cada atributo. 
# El campo letraDNI se debe calcular automáticamente (se debe buscar información en internet sobre cómo calcular 
# este campo sabiendo el número de DNI). Crear como propiedades/setters los siguientes atributos:
# ●	edad: int: Asigna el valor de edad al atributo edad de la persona.
# ●	sexo: str: Asigna el valor de sexo al atributo sexo de la persona
# ●	dni: int: Asigna el valor de dni al atributo dni de la persona. Deberá comprobar que el número introducido 
# tiene la longitud adecuada (8 como máximo y 1 como mínimo). 
# Además invocará al método calcularLetraDni()que se definirá más adelante.
# ●	peso: float: Asigna el valor de peso al atributo peso de la persona, comprobando que el valor recibido es correcto.
# ●	altura: float: Asigna el valor de altura al atributo altura de la persona, comprobando que el valor recibido es correcto.
# Crear además los siguientes métodos:
# ●	 calcularLetraDni(self): Calcula la letra del DNI en base al valor del atributo DNI de la persona, y 
# lo almacena en el atributo letraDNI.
# ●	__str_(self): Devuelve un String para imprimir por pantalla los atributos de la persona de acuerdo al siguiente formato:
# Información personal:
# Nombre: Pepe
# Sexo: Hombre
# Edad: 16 años
# DNI: 00821946-H
# Peso: 80.0 kg
# Altura: 177.0 cm
# ●	Crear un programa que cree una tupla con 3 objetos de la clase Persona en base a las siguientes reglas:
#   o	El primer objeto se creará con valores de los campos elegidos por el programador. 
#   o	El segundo objeto se creará con valores que se recibirán por el teclado.
#   o	El tercer objeto obtendrá por teclado todos los valores de los campos menos el peso, la altura y el sexo, 
#       a los que se asignarán los valores 90, 185 y femenino, respectivamente.
# ●	Por último, se mostrará la información de cada objeto por pantalla utilizando el método __str__ definido con anterioridad.
# Autor: Miguel Jun Patricio Ferrer
# Fecha: 10/11/26
# Version: 1.0
# D=================================================================================================================== #

# C=================================================================================================================== #
# Nombre de la clase: Persona 
# Descripción: Gestiona los datos de una persona y calcula su letra del DNI mediante el su número de DNI
# Autor: Miguel Jun Patricio Ferrre
# Fecha de creación: 10/11/26
# Fecha de ult. modificación: 10/11/26
# Anotaciones extra:
# C=================================================================================================================== #
class Persona:
    def __init__(self, nombre: str, edad: int, dni: int, sexo: str, peso: float, altura: float):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.__letraDNI = "" # Se calcula luego, por el momento dejar el atributo como una cadena de caracteres vacía
        self.dni = dni

    # --- PROPIEDADES ---
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad: int):
        if type(edad) != int:
            raise TypeError("La edad debe ser un número entero")
        elif edad <= 0:
            raise ValueError("La edad debe ser positiva")
        else:
            self.__edad = edad

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo: str):
        if type(sexo) != str:
            raise TypeError("El sexo debe ser texto")
        elif sexo.lower() not in ("hombre", "mujer", "no-binario"):
            raise ValueError("El sexo debe ser hombre, mujer o no-binario")
        else:
            self.__sexo = sexo.capitalize()

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni: int):
        if type(dni) != int:
            raise TypeError("El DNI debe ser un número entero")
        elif dni < 0 or dni > 99999999:
            raise ValueError("El DNI debe tener entre 1 y 8 cifras")
        else:
            self.__dni = dni
            # Cada vez que cambia el DNI, la letra se vuelve a calcular
            self.calcularLetraDni()

    # Definir a letraDNI solo con property para que sea un atributo que solo se puede leer pero no cambiar desde fuera
    @property
    def letraDNI(self):
        return self.__letraDNI

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso: float):
        if type(peso) != int and type(peso) != float:
            raise TypeError("El peso debe ser un número")
        elif peso <= 0:
            raise ValueError("El peso debe ser positivo")
        else:
            self.__peso = float(peso)

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura: float):
        if type(altura) != int and type(altura) != float:
            raise TypeError("La altura debe ser un número")
        elif altura <= 0:
            raise ValueError("La altura debe ser positiva")
        else:
            self.__altura = float(altura)

    # --- MÉTODOS ---
    def calcularLetraDni(self):
        # Calcula la letra del DNI: letra en la posición (dni % 23) de la cadena de letras oficial, y la guarda en letraDNI.
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"  # variable local, sin self
        self.__letraDNI = letras[self.dni % 23]

    def __str__(self) -> str:
        return (f"Información personal:\n"
                f"Nombre: {self.nombre}\n"
                f"Sexo: {self.sexo}\n"
                f"Edad: {self.edad} años\n"
                f"DNI: {self.dni:08d}-{self.letraDNI}\n"
                f"Peso: {self.peso} kg\n"
                f"Altura: {self.altura} cm")


