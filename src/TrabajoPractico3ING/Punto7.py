# Interfaz para la creación de dispositivos de seguridad
class FabricaDispositivosSeguridad:
    def crear_camara(self):
        pass
    
    def crear_sensor_movimiento(self):
        pass
    
    def crear_panel_alarma(self):
        pass

# Fábrica concreta para dispositivos de seguridad con protocolo Wi-Fi
class FabricaWifiDispositivosSeguridad(FabricaDispositivosSeguridad):
    def crear_camara(self):
        return CamaraWifi()
    
    def crear_sensor_movimiento(self):
        return SensorMovimientoWifi()
    
    def crear_panel_alarma(self):
        return PanelAlarmaWifi()

# Clases para los diferentes dispositivos de seguridad
class Camara:
    def capturar(self):
        pass

class SensorMovimiento:
    def detectar_movimiento(self):
        pass

class PanelAlarma:
    def activar_alarma(self):
        pass

# Implementaciones concretas de los dispositivos de seguridad para protocolo Wi-Fi
class CamaraWifi(Camara):
    def capturar(self):
        print("Capturando transmisión de video a través de Wi-Fi")

class SensorMovimientoWifi(SensorMovimiento):
    def detectar_movimiento(self):
        print("Detectando movimiento usando Wi-Fi")

class PanelAlarmaWifi(PanelAlarma):
    def activar_alarma(self):
        print("Activando panel de alarma sobre Wi-Fi")

# Ejemplo
if __name__ == "__main__":
    fabrica_wifi = FabricaWifiDispositivosSeguridad()  # Selecciona la fábrica de dispositivos Wi-Fi

    # Crear dispositivos de seguridad
    camara_wifi = fabrica_wifi.crear_camara()
    sensor_movimiento_wifi = fabrica_wifi.crear_sensor_movimiento()
    panel_alarma_wifi = fabrica_wifi.crear_panel_alarma()

    # Utilizar los dispositivos de seguridad
    camara_wifi.capturar()
    sensor_movimiento_wifi.detectar_movimiento()
    panel_alarma_wifi.activar_alarma()
