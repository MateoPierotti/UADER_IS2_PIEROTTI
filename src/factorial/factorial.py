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
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    if start > end:
        print("El primer número debe ser menor o igual que el segundo número.")
        sys.exit()
    
    print("Factoriales dentro del rango", start, "-", end, ":")
    for num in range(start, end + 1):
        print("Factorial de", num, "es", factorial(num))

