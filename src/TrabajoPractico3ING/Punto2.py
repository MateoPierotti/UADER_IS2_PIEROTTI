# Singleton
class CalculadoraImpuestos:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def calcular_impuestos(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones_municipales = base_imponible * 0.012
        total_impuestos = iva + iibb + contribuciones_municipales
        return total_impuestos
    
calculadora_impuesto = CalculadoraImpuestos()
base_inponible = 1000

impuestos_a_calcular = calculadora_impuesto.calcular_impuestos(base_inponible)
print("Impuestos calculados:", impuestos_a_calcular)