# factory
from abc import ABC, abstractmethod

class Factura(ABC):
    def __init__(self, importe):
        self.importe = importe

    @abstractmethod
    def generar_factura(self):
        pass

class FacturaIVAResponsable(Factura):
    def generar_factura(self):
        return f"Factura con importe total: {self.importe}, Condición impositiva: IVA Responsable"

class FacturaIVANoInscripto(Factura):
    def generar_factura(self):
        return f"Factura con importe total: {self.importe}, Condición impositiva: IVA No Inscripto"

class FacturaIVAExento(Factura):
    def generar_factura(self):
        return f"Factura con importe total: {self.importe}, Condición impositiva: IVA Exento"

class FacturaFactory:
    def crear_factura(self, importe, condicion_impositiva):
        if condicion_impositiva == "IVA Responsable":
            return FacturaIVAResponsable(importe)
        elif condicion_impositiva == "IVA No Inscripto":
            return FacturaIVANoInscripto(importe)
        elif condicion_impositiva == "IVA Exento":
            return FacturaIVAExento(importe)
        else:
            raise ValueError("Condición impositiva no válida")

# Ejemplo de uso
factory = FacturaFactory()

# Crear factura para un cliente con IVA Responsable
factura_iva_responsable = factory.crear_factura(1000, "IVA Responsable")
print(factura_iva_responsable.generar_factura())

# Crear factura para un cliente con IVA No Inscripto
factura_iva_no_inscripto = factory.crear_factura(1500, "IVA No Inscripto")
print(factura_iva_no_inscripto.generar_factura())

# Crear factura para un cliente con IVA Exento
factura_iva_exento = factory.crear_factura(800, "IVA Exento")
print(factura_iva_exento.generar_factura())
