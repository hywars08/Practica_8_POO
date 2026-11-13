# D=================================================================================================================== #
# Título: Ejercicio 5.	
# Crea una clase CuentaBancaria con las siguientes características:
# Atributos:
# ●	titular: str. 
# ●	saldo: float. 
# ●	movimientos: list. Atributo con la lista de movimientos en la cuenta.
# 	 Métodos especiales:
# ●	init:  recibirá el nombre del titular. Establecerá a 0.0 el saldo inicial e inicializará la lista de movimientos 
#   como una lista vacía.
# ●	str: Devuelve un String para imprimir los datos de la cuenta siguiendo el siguiente formato 
#   (los últimos movimientos son hasta un máximo de 10):
# 
# 
# 
# Información de la cuenta:
# Titular: Pepe
# Saldo: 649.9 €
# Últimos movimientos:
#    Tipo   |      Concepto      | Importe  |  Saldo   
#  Retirada |       Seguro       |    -200.4|     649.9
#  Ingreso  |    Sin Concepto    |     350.3|     850.3
#  Ingreso  |        Paga        |     500.0|     500.0
# 	Otros métodos:
# ●	ingresar(importe, concepto:str): Método que realiza un ingreso en la cuenta. Se validará el importe. 
#   El método actualiza el saldo y genera un movimiento.
# ●	retirar(importe, concepto:str): Método que realiza una retirada de saldo en la cuenta. 
#   Se validará el importe y que se tiene saldo suficiente. El método actualiza el saldo y genera un movimiento.
# ●	Se pueden crear métodos auxiliares para facilitar la creación de la lista de movimientos 
#   y mostrar los 10 últimos movimientos
# Autor: Miguel Jun Patricio Ferrer
# Fecha: 10/11/26
# Version: 1.0
# D=================================================================================================================== #

# C=================================================================================================================== #
# Nombre de la clase: CuentaBancaria
# Descripción: Gestiona la cuenta bancaria de una persona guardando su nombre. Además de manegar su sueldo, ingresos y salidas
# y poder mostrar los últimos movimientos
# Autor: Miguel Jun Patricio Ferrer
# Fecha de creación: 10/11/26
# Fecha de ult. modificación: 10/11/26
# Anotaciones extra:
# C=================================================================================================================== #

class CuentaBancaria:
    def __init__(self, titular: str):
        # Atributo con property + setter: se valida también al crear el objeto
        self.titular = titular
        # saldo y movimientos son de solo lectura desde fuera (property sin setter)
        self.__saldo = 0.0
        self.__movimientos = []

    # --- PROPIEDADES ---
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular: str):
        if type(titular) != str:
            raise TypeError("El titular debe ser texto")
        elif len(titular) < 1:
            raise ValueError("El titular debe tener al menos un carácter")
        else:
            self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def movimientos(self):
        return self.__movimientos

    # --- MÉTODOS PRIVADOS AUXILIARES --- # Solo son se pueden utilizar internamente en la clase
    def __ValidarImporte(self, importe):
        if type(importe) != int and type(importe) != float:
            raise TypeError("El importe debe ser un número")
        elif importe <= 0:
            raise ValueError("El importe debe ser positivo")

    # Sirve para guardar el movimiento realizado una 
    def __RegistrarMovimiento(self, tipo: str, concepto: str, importe: float):
        movimiento = {"tipo": tipo, "concepto": concepto, "importe": importe, "saldo": self.__saldo} # El movimiento es un diccionario
        self.__movimientos.append(movimiento)

    def __UltimosMovimientos(self):
        lineas = "" # Cadena de caractéres vacía
        # Calcular los últimos movimientos
        ultimos_movimientos = self.__movimientos[-10:] # Crear una nueva lista que empieze desde empieze desde el decimo elemento de la lista empezando por atras
        ultimos_movimientos.reverse() # Darle la vuelta a la lista para que se muestre primero el último movimiento y no al revés
        # Bucle que recorre los últimos movimientos
        for movimiento in ultimos_movimientos:
            lineas += (f"{movimiento["tipo"]:^10}|{movimiento["concepto"]:^20}|"f"{movimiento["importe"]:>10}|{movimiento["saldo"]:>10}\n") # Movimiento maquetado. Donde apunta el simbolo es donde rellena huecos :>
        return lineas

    # --- MÉTODOS PÚBLICOS ---
    def Ingresar(self, importe, concepto: str = "Sin Concepto"): # El concepto por defecto es "Sin Concepto"
        self.__ValidarImporte(importe) # Validar que el importe introducido sea correcto (forzarlo a pasar por el property, setter)
        self.__saldo = round(self.__saldo + importe, 2) # Sumar al saldo el importe introducido
        self.__RegistrarMovimiento("Ingreso", concepto, importe)

    def Retirar(self, importe, concepto: str = "Sin Concepto"): # El concepto por defecto es "Sin Concepto"
        self.__ValidarImporte(importe)
        if importe > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo = round(self.__saldo - importe, 2)
        self.__RegistrarMovimiento("Retirada", concepto, -importe)

    def __str__(self):
        return (f"Información de la cuenta:\n"
                f"Titular: {self.titular}\n"
                f"Saldo: {self.saldo} €\n"
                f"Últimos movimientos:\n"
                f"{'Tipo':^10}|{'Concepto':^20}|{'Importe':^10}|{'Saldo':^10}\n" # el :^numero srive para dejar en medio los
                f"{self.__UltimosMovimientos()}")