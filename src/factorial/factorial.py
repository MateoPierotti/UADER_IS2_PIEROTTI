#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Función para calcular el factorial de un número
def factorial(num): 
    # Si el número es negativo, imprime un mensaje de error
    if num < 0: 
        print("Factorial de un número negativo no existe")

    # Si el número es 0, el factorial es 1
    elif num == 0: 
        return 1
        
    else: 
        # Calcula el factorial del número
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Verifica si se proporcionaron dos números como argumentos de línea de comandos
if len(sys.argv) != 3:
    print("Debe informar dos números para formar un rango.")
    sys.exit() # Sale del programa si no se proporcionan dos números

else:
    # Convierte los argumentos en enteros
    desde = int(sys.argv[1])
    hasta = int(sys.argv[2])

    # Verifica que los límites estén dentro del rango permitido
    if desde < 1:
        print("El límite inferior (desde) debe ser al menos 1.")
        sys.exit() # Sale del programa si el límite inferior es menor que 1
    elif hasta > 60:
        print("El límite superior (hasta) no puede ser mayor que 60.")
        sys.exit() # Sale del programa si el límite superior es mayor que 60
    elif desde > hasta:
        print("El límite inferior (desde) no puede ser mayor que el límite superior (hasta).")
        sys.exit() # Sale del programa si el límite inferior es mayor que el límite superior
    
    # Calcular los factoriales dentro del rango establecido
    print("Factoriales dentro del rango", desde, "-", hasta, ":")
    for num in range(desde, hasta + 1):
        print("Factorial de", num, "es", factorial(num))
