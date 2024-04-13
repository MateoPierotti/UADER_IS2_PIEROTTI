# Clase Flyweight que almacena las propiedades comunes
class InformacionComunTicket:
    def __init__(self, nombre_cliente, fecha_creacion):
        self.nombre_cliente = nombre_cliente
        self.fecha_creacion = fecha_creacion

# Clase Ticket que hace referencia al Flyweight
class Ticket:
    def __init__(self, informacion_comun, tipo_problema, prioridad):
        self.informacion_comun = informacion_comun
        self.tipo_problema = tipo_problema
        self.prioridad = prioridad

    def mostrar_informacion(self):
        print("Información común:")
        print(f"Nombre del cliente: {self.informacion_comun.nombre_cliente}")
        print(f"Fecha de creación: {self.informacion_comun.fecha_creacion}")
        print("Información unica:")
        print(f"Tipo de problema: {self.tipo_problema}")
        print(f"Prioridad: {self.prioridad}")

# Cliente: creación de tickets
if __name__ == "__main__":
    # Crear información común (Flyweight)
    informacion_comun1 = InformacionComunTicket("Cliente A", "2024-04-15")
    informacion_comun2 = InformacionComunTicket("Cliente B", "2024-04-16")

    # Crear tickets que hacen referencia al Flyweight
    ticket1 = Ticket(informacion_comun1, "Problema de red", "Alta")
    ticket2 = Ticket(informacion_comun1, "Problema de software", "Media")
    ticket3 = Ticket(informacion_comun2, "Problema de hardware", "Baja")

    # Mostrar información de los tickets
    ticket1.mostrar_informacion()
    print("\n")
    ticket2.mostrar_informacion()
    print("\n")
    ticket3.mostrar_informacion()
