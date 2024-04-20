class IteradorReverso:
    def __init__(self, data):
        """
        Constructor de la clase IteradorReverso.

        Parameters:
        data (str): La cadena de caracteres a almacenar.
        """
        self.data = data
        self.indice = len(data)

    def __iter__(self):
        """
        Método especial para obtener un iterador.
        """
        return self

    def __next__(self):
        """
        Método especial para obtener el próximo elemento del iterador.
        """
        if self.indice == 0:
            raise StopIteration
        self.indice -= 1
        return self.data[self.indice]


class IteradorDirecto:
    def __init__(self, data):
        """
        Constructor de la clase IteradorDirecto.

        Parameters:
        data (str): La cadena de caracteres a almacenar.
        """
        self.data = data
        self.indice = 0

    def __iter__(self):
        """
        Método especial para obtener un iterador.
        """
        return self

    def __next__(self):
        """
        Método especial para obtener el próximo elemento del iterador.
        """
        if self.indice == len(self.data):
            raise StopIteration
        self.indice += 1
        return self.data[self.indice - 1]


class IteradorBidireccional:
    def __init__(self, data):
        """
        Constructor de la clase IteradorBidireccional.

        Parameters:
        data (str): La cadena de caracteres a almacenar.
        """
        self.data = data

    def iterador_directo(self):
        """
        Método para obtener un iterador en sentido directo.
        """
        return IteradorDirecto(self.data)

    def iterador_reverso(self):
        """
        Método para obtener un iterador en sentido inverso.
        """
        return IteradorReverso(self.data)


# Ejemplo de uso
if __name__ == "__main__":
    cadena = "Hola Mundo" 
    
    print("Recorrido en sentido directo:")
    iterador_directo = IteradorDirecto(cadena)
    for caracter in iterador_directo:
        print(caracter)

    print("\nRecorrido en sentido inverso:")
    iterador_reverso = IteradorReverso(cadena)
    for caracter in iterador_reverso:
        print(caracter)
