#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) != 3:
    print("Debe informar dos números para formar un rango.")
    sys.exit()
else:
    desde = int(sys.argv[1])
    hasta = int(sys.argv[2])

    if desde < 1:
        print("El límite inferior (desde) debe ser al menos 1.")
        sys.exit()
    elif hasta > 60:
        print("El límite superior (hasta) no puede ser mayor que 60.")
        sys.exit()
    elif desde > hasta:
        print("El límite inferior (desde) no puede ser mayor que el límite superior (hasta).")
        sys.exit()
    
    # Calcular los factoriales dentro del rango establecido
    print("Factoriales dentro del rango", desde, "-", hasta, ":")
    for num in range(desde, hasta + 1):
        print("Factorial de", num, "es", factorial(num))

