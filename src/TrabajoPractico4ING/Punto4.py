# Componente base: Numero
class Numero:
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        print(f"Valor: {self.valor}")


# Decorador base: DecoradorNumero
class DecoradorNumero(Numero):
    def __init__(self, numero):
        self.numero = numero

    def imprimir(self):
        self.numero.imprimir()


# Decoradores con funcionalidades adicionales
class SumarDos(DecoradorNumero):
    def imprimir(self):
        super().imprimir()
        print(f"Sumar 2: {self.numero.valor + 2}")


class MultiplicarPorDos(DecoradorNumero):
    def imprimir(self):
        super().imprimir()
        print(f"Multiplicar por 2: {self.numero.valor * 2}")


class DividirPorTres(DecoradorNumero):
    def imprimir(self):
        super().imprimir()
        print(f"Dividir por 3: {self.numero.valor / 3}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un número inicial
    numero = Numero(10)
    print("Número sin decoradores:")
    numero.imprimir()

    # Agregar decoradores para sumar 2, multiplicar por 2 y dividir por 3
    numero_decorado = DividirPorTres(numero)
    numero_decorad = MultiplicarPorDos(numero)
    numero_decora = SumarDos(numero)

    print("\nNúmero con decoradores:")
    numero_decorado.imprimir()
    numero_decorad.imprimir()
    numero_decora.imprimir()