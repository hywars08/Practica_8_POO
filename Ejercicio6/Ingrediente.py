# D=================================================================================================================== #
# Título: Ejercicio 6.	
# Crear clases para los objetos del proyecto final. Para cada clase crear el método init y las propiedades y setters 
# necesarios.
# Autor: Miguel Jun Patricio Ferrer
# Fecha: 10/11/26
# Version: 1.0
# D=================================================================================================================== #

# C=================================================================================================================== #
# Nombre de la clase: Ingrediente
# Descripción: Gestiona los ingredientes (futura clase madre) con los siguientes atributos (su nombre, y los diferentes estados
# como si esta cortado, triturado, cocinado...)
# Autor: Miguel Jun Patricio Ferrer
# Fecha de creación: 10/11/26
# Fecha de ult. modificación: 10/11/26
# Anotaciones extra:
# C=================================================================================================================== #

# Estados posibles de un ingrediente (constantes)
ENTERO = "entero"
CORTADO = "cortado"
TRITURADO = "triturado"


class Ingrediente:
    def __init__(self, nombre, necesita_corte):
        self.__nombre = nombre
        self.__necesita_corte = necesita_corte
        self.__forma = ENTERO
        self.__cocinado = False

    @property
    def nombre(self):
        return self.__nombre

    @property
    def necesita_corte(self):
        return self.__necesita_corte

    @property
    def forma(self):
        return self.__forma

    @property
    def cocinado(self):
        return self.__cocinado

    def Cortar(self):
        if self.__necesita_corte and self.__forma == ENTERO:
            self.__forma = CORTADO

    def Triturar(self):
        self.__forma = TRITURADO

    def Cocinar(self):
        self.__cocinado = True