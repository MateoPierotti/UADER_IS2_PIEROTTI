# Singleton
class SingletonFactorial:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)


def obtener_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero para calcular su factorial: "))
            if numero < 0:
                print("El número debe ser mayor o igual a cero.")
            else:
                return numero
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


singleton_factorial = SingletonFactorial()

numero = obtener_numero()

resultado = singleton_factorial.factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
