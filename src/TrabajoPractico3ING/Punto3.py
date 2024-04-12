# factory
from abc import ABC, abstractmethod

class Hamburguesa(ABC):
    @abstractmethod
    def entregar(self):
        pass

class HamburguesaMostrador(Hamburguesa):
    def entregar(self):
        return "Hamburguesa entregada en el mostrador"

class HamburguesaCliente(Hamburguesa):
    def entregar(self):
        return "Hamburguesa entregada al cliente"

class HamburguesaDelivery(Hamburguesa):
    def entregar(self):
        return "Hamburguesa enviada por delivery"

class HamburguesaFactory:
    def crear_hamburguesa(self, tipo):
        if tipo == "mostrador":
            return HamburguesaMostrador()
        elif tipo == "cliente":
            return HamburguesaCliente()
        elif tipo == "delivery":
            return HamburguesaDelivery()
        else:
            raise ValueError("Tipo de entrega de hamburguesa no válido")


factory = HamburguesaFactory()

# Crear y entregar una hamburguesa en el mostrador
hamburguesa_mostrador = factory.crear_hamburguesa("mostrador")
print(hamburguesa_mostrador.entregar())

# Crear y entregar una hamburguesa al cliente
hamburguesa_cliente = factory.crear_hamburguesa("cliente")
print(hamburguesa_cliente.entregar())

# Crear y enviar una hamburguesa por delivery
hamburguesa_delivery = factory.crear_hamburguesa("delivery")
print(hamburguesa_delivery.entregar())