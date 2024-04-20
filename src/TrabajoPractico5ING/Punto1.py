class Handler:
    def __init__(self, successor=None):
        """
        Constructor de la clase Handler.

        Parameters:
        successor (Handler): El sucesor en la cadena de responsabilidad.
        """
        self.successor = successor

    def handle(self, number):
        """
        Método para manejar el número.

        Parameters:
        number (int): El número a manejar.
        """
        if self.successor:
            self.successor.handle(number)

    def is_consumed(self, number):
        """
        Método para determinar si el número ha sido consumido.

        Parameters:
        number (int): El número a verificar si ha sido consumido.
        """
        pass


class PrimeHandler(Handler):
    def is_prime(self, number):
        """
        Método para verificar si un número es primo.

        Parameters:
        number (int): El número a verificar.

        Returns:
        bool: True si el número es primo, False de lo contrario.
        """
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_consumed(self, number):
        """
        Método para consumir el número si es primo o pasar al siguiente manejador.

        Parameters:
        number (int): El número a manejar.
        """
        if self.is_prime(number):
            print(f"PrimeHandler consumió el número primo: {number}")
        else:
            super().handle(number)


class EvenHandler(Handler):
    def is_consumed(self, number):
        """
        Método para consumir el número si es par o pasar al siguiente manejador.

        Parameters:
        number (int): El número a manejar.
        """
        if number % 2 == 0:
            print(f"EvenHandler consumió el número par: {number}")
        else:
            super().handle(number)


class NumberProcessor:
    def __init__(self):
        """
        Constructor de la clase NumberProcessor.
        """
        # Configurar la cadena de manejo
        self.handler_chain = PrimeHandler(EvenHandler())

    def process_numbers(self):
        """
        Método para procesar los números del 1 al 100.
        """
        for number in range(1, 101):
            self.handler_chain.handle(number)


if __name__ == "__main__":
    processor = NumberProcessor()
    processor.process_numbers()

    # Prueba de números primos y pares
    for i in range(1, 101):
        consumido = False
        if PrimeHandler().is_prime(i):
            print(f"{i} es un número primo.")
            consumido = True
        elif i % 2 == 0:
            print(f"{i} es un número par.")
            consumido = True

        if not consumido:
            print(f"{i} no fue consumido por ningún manejador.")
