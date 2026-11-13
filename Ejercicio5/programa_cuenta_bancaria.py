from CuentaBancaria import CuentaBancaria # Llamar a la clase CuentaBancaria desde el fichero "CuentaBancaria"

# Añadir los movimientos especificados en el ejemplo de la práctica
cuenta = CuentaBancaria("Pepe")
cuenta.Ingresar(500.0, "Paga")
cuenta.Ingresar(350.3)
cuenta.Retirar(200.4, "Seguro")
print(cuenta)

# Probar que el método de que muestra los últimos movimientos, solo muestra los 10 últimos, no todos
for i in range(1, 13):
    cuenta.Ingresar(1, f"Extra {i}") # Crear 13 nuevos ingresos de 1 euro
print(cuenta) # Imprimir la cuenta 
