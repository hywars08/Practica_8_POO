# D=================================================================================================================== #
# Título: Ejercicio 3.	
# Crear una clase que represente un intervalo temporal:
# ●	Un intervalo temporal se representa por un instante inicial (horas y minutos) y un instante final (horas y minutos)
# ●	Crear un método init que reciba valores para las horas y los minutos del intervalo. El instante inicial debe ser anterior al instante final, en caso contrario se intercambiarán.
# ●	Crear propiedades y setters para comprobar que los valores recibidos son correctos.
# ●	Crear métodos para comparar intervalos. Un intervalo es menor si su duración es menor.
# ●	Crear un método __str__. Debe devolver información sobre si el intervalo pertenece a la mañana (6:00 a 12:00), la tarde (12:00 a 18:00), la noche (18:00 a 0:00) o la madrugada (0:00 a 6:00). Nótese que un intervalo temporal puede pertenecer a varias de las categorías anteriores. Por ejemplo, el intervalo que va desde las 21:00 a las 23:15 pertenece únicamente a la noche, pero el que va de las 11:00 a las 19:00 pertenece a la mañana, la tarde y la noche.
# ●	Crear un programa que le pregunte al usuario cuántos intervalos temporales quiere y los guarde en una lista. Si el intervalo temporal definido por el usuario ya existe en la lista, deberá indicarlo y solicitar uno nuevo, en caso contrario lo guardará en la lista en según su duración, primero los más cortos. Para finalizar debe imprimir los intervalos como sigue:
# Intervalo temporal: [11:59-12:18]
# Pertenece a: mañana	tarde

# Autor: Miguel Jun Patricio Ferrer
# Fecha: 10/11/26
# Version: 1.0
# D=================================================================================================================== #

# C=================================================================================================================== #
# Nombre de la clase: IntervaloTemporal
# Descripción: Gestiona datos de un intervalo temporal y calcula en que franja horaria está el intervalo
# Autor: Miguel Jun Patricio Ferrer
# Fecha de creación: 11/11/26
# Fecha de ult. modificación: 11/11/26
# Anotaciones extra:
# C=================================================================================================================== #
class IntervaloTemporal:
    def __init__(self, hora_inicio: int, minuto_inicio: int, hora_fin: int, minuto_fin: int):
        self.hora_inicio = hora_inicio
        self.minuto_inicio = minuto_inicio
        self.hora_fin = hora_fin
        self.minuto_fin = minuto_fin
        # El inicial debe ser anterior al final; si no, se intercambian
        if self.__InicioEnMinutos() > self.__FinEnMinutos():
            self.hora_inicio = self.hora_fin
            self.hora_fin = self.hora_inicio
            self.minuto_inicio = self.minuto_fin 
            self.minuto_fin = self.minuto_inicio

    # --- MÉTODOS PRIVADOS AUXILIARES ---
    def __ValidarHora(self, hora):
        if type(hora) != int:
            raise TypeError("La hora debe ser un número entero")
        elif hora < 0 or hora > 23:
            raise ValueError("La hora debe estar entre 0 y 23")

    def __ValidarMinuto(self, minuto):
        if type(minuto) != int:
            raise TypeError("Los minutos deben ser un número entero")
        elif minuto < 0 or minuto > 59:
            raise ValueError("Los minutos deben estar entre 0 y 59")

    def __InicioEnMinutos(self):
        return self.hora_inicio * 60 + self.minuto_inicio

    def __FinEnMinutos(self):
        return self.hora_fin * 60 + self.minuto_fin

    def __Franjas(self):
        # Devuelve a la franja del día que pertenece el intervalo
        franjas = {"madrugada": (0, 360), 
                   "mañana": (360, 720),
                   "tarde": (720, 1080), 
                   "noche": (1080, 1440)}
        inicio = self.__InicioEnMinutos() # Calcula cuando empieza el intervalo en minutos
        fin = self.__FinEnMinutos() # Calcula cuando termina el intervalo en minutos
        resultado = []

        # Bucle que recorre las claves del diccionario franjas
        for nombre in franjas:
            desde = franjas[nombre][0] # Primer elemento (inicio de la franja)
            hasta = franjas[nombre][1] # Segundo elemento (final de la franja)
            # Un intervalo pertenece a una franja si su inicio es menor que el el fin de la franja y su final mayor que la franja 
            # O si el inicio y final del intervalo es el mismo se comprueba si el inicio y el final estan entre la franja especifica
            if (inicio < hasta and fin > desde) or (inicio == fin and desde <= inicio and inicio < hasta):
                resultado.append(nombre)
        return resultado

    # --- PROPIEDADES ---
    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, hora: int):
        self.__ValidarHora(hora)
        self.__hora_inicio = hora

    @property
    def minuto_inicio(self):
        return self.__minuto_inicio

    @minuto_inicio.setter
    def minuto_inicio(self, minuto: int):
        self.__ValidarMinuto(minuto)
        self.__minuto_inicio = minuto

    @property
    def hora_fin(self):
        return self.__hora_fin

    @hora_fin.setter
    def hora_fin(self, hora: int):
        self.__ValidarHora(hora)
        self.__hora_fin = hora

    @property
    def minuto_fin(self):
        return self.__minuto_fin

    @minuto_fin.setter
    def minuto_fin(self, minuto: int):
        self.__ValidarMinuto(minuto)
        self.__minuto_fin = minuto

    # --- MÉTODOS ---
    def Duracion(self):
        # Devuelve la duración del intervalo en minutos
        return self.__FinEnMinutos() - self.__InicioEnMinutos()

    def __eq__(self, otro):
        # Mismo intervalo = mismo inicio y mismo final
        return (self.hora_inicio == otro.hora_inicio and self.minuto_inicio == otro.minuto_inicio and self.hora_fin == otro.hora_fin and self.minuto_fin == otro.minuto_fin)

    def __lt__(self, otro):
        # Un intervalo es menor si su duración es menor
        return self.Duracion() < otro.Duracion()

    def __gt__(self, otro):
        return self.Duracion() > otro.Duracion()

    def __str__(self):
        return (f"Intervalo temporal: [{self.hora_inicio:02d}:{self.minuto_inicio:02d}-{self.hora_fin:02d}:{self.minuto_fin:02d}]\n"
                f"Pertenece a: {(self.__Franjas())}")