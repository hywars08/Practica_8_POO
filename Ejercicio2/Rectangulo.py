# D=================================================================================================================== #
# Título: Ejercicio 2.	
# Crear una clase Rectángulo con tres atributos: base, altura y cuadrado (que especifica si además de rectángulo es un cuadrado o no) 
# ●	Crear propiedades y setters para cambiar y leer el valor de los atributos 
# (decidir cuáles se deben poder especificar externamente y cuáles se pueden calcular automáticamente. 
# Decidir también los valores válidos para cada uno de ellos).
# ●	Crear un método str que devuelve un String del tipo: “un <rectángulo/cuadrado> de base <base> y altura <altura>” 
# donde los elementos entre <> deben cambiarse por los valores adecuados.
# ●	Crear un método eq que compara dos rectángulos y devuelve true si ambos tienen la misma base y la misma altura, 
# considerando que un rectángulo de (base, altura) es igual que uno de (altura, base).
# ●	Crear un método perimetro que devuelve el perímetro del Rectángulo.
# ●	Crear un método area que devuelve el área del Rectángulo.
# ●	Crear un método que devuelve el valor del lado mayor del rectángulo (la altura o la base)
# ●	Crear un método que convierte un rectángulo en un cuadrado. Deberá convertir la base o la altura al valor mayor de ambos. 
#   Devolverá True si lo que se cambió fue la base y False si lo que se cambió fue la altura.
# ●	Crear un método para comparar rectángulos usando operadores relacionales. Un rectángulo es mayor que otro si su lado más 
#   grande es mayor.
# ●	En una clase principal crear una lista de Rectángulos con un número aleatorio de entre 10 y 1000 elementos. 
#   Crear los rectángulos de la lista con dimensiones enteras entre 1 y 10. 
#   Imprimir los que sean cuadrados, los de mayor área, los de mayor perímetro y los de lado más grande. 
#   Convertir los de mayor lado a cuadrados, especificando si lo que se ha cambiado es la base o la altura.
# Autor: Miguel Jun Patricio Ferrer
# Fecha: 10/11/26
# Version: 1.0
# D=================================================================================================================== #

# C=================================================================================================================== #
# Nombre de la clase: Rectángulo 
# Descripción: Gestiona rectángulos en funcion de la base y la altura al que se fije el objeto. Tiene diversos métodos.
# Autor: Miguel Jun Patricio Ferrer
# Fecha de creación: 10/11/26
# Fecha de ult. modificación: 10/11/26
# Anotaciones extra:
# C=================================================================================================================== #
class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    # --- PROPIEDADES ---
    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base: float):
        if type(base) != int and type(base) != float:
            raise TypeError("La base debe ser un número")
        elif base <= 0:
            raise ValueError("La base debe ser positiva")
        else:
            self.__base = base

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
            self.__altura = altura

    # Definir un método que devuelve si es un cuadrado o no el objeto. Se usa property para leerlo como un atributo evitar que se modifique desde fuera y solo se pueda leer
    @property
    def cuadrado(self):
        return self.base == self.altura

    # --- MÉTODOS ---
    def Perimetro(self):
        return 2 * (self.base + self.altura)

    def Area(self):
        return self.base * self.altura

    def LadoMayor(self):
        if self.base >= self.altura:
            mayor = self.base
        else:
            mayor = self.altura
        return mayor
    
    # Iguala el todos los lados al mayor, luego devuelve si era un cuadrado, o lo ha cambiado
    def ConvertirEnCuadrado(self): 
        if self.base < self.altura:
            self.base = self.altura
            cambio_base = True
        else:
            self.altura = self.base
            cambio_base = False
        return cambio_base

    # Definir como funciona el "print" de un objeto
    def __str__(self):
        if self.cuadrado:
            tipo = "cuadrado"
        else:
            tipo = "rectángulo"
        return (f"un <{tipo}> de base <{self.base}> y altura <{self.altura}>")

    # Definir como funciona el operador == 
    def __eq__(self, otro):
        # Dos rectángulos son iguales  si tiene la base y la altura igual entre sí o la base1 = altura2 y la altura1 = base2
        return ((self.base == otro.base and self.altura == otro.altura) or (self.base == otro.altura and self.altura == otro.base))

    # Definir como funciona el operador >
    def __gt__(self, otro):
        return self.LadoMayor() > otro.LadoMayor()

    # Definir como funciona el operador <
    def __lt__(self, otro):
        return self.LadoMayor() < otro.LadoMayor()