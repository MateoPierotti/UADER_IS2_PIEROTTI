# Abstracción: ProductoLaminas
class ProductoLaminas:
    def __init__(self, espesor, ancho, laminador):
        self.espesor = espesor
        self.ancho = ancho
        self.laminador = laminador

    def producir(self):
        self.laminador.producir_laminas(self.espesor, self.ancho)


# Implementación: Laminador
class Laminador:
    def producir_laminas(self, espesor, ancho):
        pass

# Implementaciones específicas de Laminador

class Laminador5Metros(Laminador):
    def producir_laminas(self, espesor, ancho):
        print(f"Produciendo láminas de {espesor} pulgadas de espesor y {ancho} metros de ancho en el laminador de 5 metros")

class Laminador10Metros(Laminador):
    def producir_laminas(self, espesor, ancho):
        print(f"Produciendo láminas de {espesor} pulgadas de espesor y {ancho} metros de ancho en el laminador de 10 metros")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de las implementaciones específicas de Laminador
    laminador_5_metros = Laminador5Metros()
    laminador_10_metros = Laminador10Metros()

    # Crear productos de láminas y asignarles el laminador correspondiente
    producto_laminas_5_metros = ProductoLaminas(0.5, 1.5, laminador_5_metros)
    producto_laminas_10_metros = ProductoLaminas(0.5, 1.5, laminador_10_metros)

    # Producir láminas utilizando los laminadores respectivos
    producto_laminas_5_metros.producir()
    producto_laminas_10_metros.producir()
