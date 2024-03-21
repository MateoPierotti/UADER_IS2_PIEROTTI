import sys

class Factorial:
    def calcular_factorial(self, num): 
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

    def run(self, desde, hasta):
        if desde < 1:
            print("El límite inferior (desde) debe ser al menos 1.")
            return
        elif hasta > 60:
            print("El límite superior (hasta) no puede ser mayor que 60.")
            return
        elif desde > hasta:
            print("El límite inferior (desde) no puede ser mayor que el límite superior (hasta).")
            return
        
    # factorial sin limite entre 1 y 60
    # def run(self, desde, hasta):
    #     if desde > hasta:
    #         print("El límite inferior (desde) no puede ser mayor que el límite superior (hasta).")
    #         return
        print("Factoriales dentro del rango", desde, "-", hasta, ":")
        for num in range(desde, hasta + 1):
            print("Factorial de", num, "es", self.calcular_factorial(num))

if __name__ == "__main__":
    # Verifica si se proporcionaron dos números como argumentos de línea de comandos
    if len(sys.argv) != 3:
        print("Debe informar dos números para formar un rango.")
    else:
        # Convierte los argumentos en enteros
        desde = int(sys.argv[1])
        hasta = int(sys.argv[2])

        factorial_calculator = Factorial()
        factorial_calculator.run(desde, hasta)
