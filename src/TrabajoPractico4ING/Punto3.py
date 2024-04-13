# Componente: Pieza
class Pieza:
    def mostrar(self):
        pass

# Hoja: PiezaSimple
class PiezaSimple(Pieza):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(f"Pieza simple: {self.nombre}")

# Compuesto: ConjuntoPiezas
class ConjuntoPiezas(Pieza):
    def __init__(self, nombre):
        self.nombre = nombre
        self.piezas = []

    def agregar_pieza(self, pieza):
        self.piezas.append(pieza)

    def mostrar(self):
        print(f"Conjunto de piezas: {self.nombre}")
        for pieza in self.piezas:
            pieza.mostrar()


# Ejemplo de uso
if __name__ == "__main__":
    # Crear el producto principal
    producto_principal = ConjuntoPiezas("Producto Principal")

    # Crear tres sub-conjuntos con cuatro piezas cada uno
    for i in range(3):
        subconjunto = ConjuntoPiezas(f"Sub-Conjunto {i+1}")
        for j in range(4):
            subconjunto.agregar_pieza(PiezaSimple(f"Pieza {j+1}"))
        producto_principal.agregar_pieza(subconjunto)

    # Mostrar el producto principal
    producto_principal.mostrar()

    # Agregar un sub-conjunto opcional con cuatro piezas
    subconjunto_opcional = ConjuntoPiezas("Sub-Conjunto Opcional")
    for i in range(4):
        subconjunto_opcional.agregar_pieza(PiezaSimple(f"Pieza Opcional {i+1}"))
    producto_principal.agregar_pieza(subconjunto_opcional)

    # Mostrar nuevamente el producto principal con el sub-conjunto opcional
    print("=" * 50)
    producto_principal.mostrar()
