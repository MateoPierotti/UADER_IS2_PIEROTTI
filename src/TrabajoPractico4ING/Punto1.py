import subprocess

# Interfaz que define la operación de ping
class InterfazPing:
    def ejecutar(self, direccion_ip):
        pass

# Clase concreta que implementa la operación de ping
class Ping(InterfazPing):
    def ejecutar(self, direccion_ip):
        if direccion_ip.startswith("192."):
            print(f"Haciendo ping a {direccion_ip}...")
            for _ in range(10):
                respuesta = subprocess.run(["ping", "-n", "1", direccion_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if respuesta.returncode == 0:
                    print(f"{direccion_ip} está alcanzable")
                else:
                    print(f"{direccion_ip} no está alcanzable")
        else:
            print("La dirección IP no es válida para este ping")

    def ejecutar_libre(self, direccion_ip):
        print(f"Haciendo ping a {direccion_ip}...")
        for _ in range(10):
            respuesta = subprocess.run(["ping", "-n", "1", direccion_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if respuesta.returncode == 0:
                print(f"{direccion_ip} está alcanzable")
            else:
                print(f"{direccion_ip} no está alcanzable")

# Proxy que envuelve a la clase Ping
class ProxyPing(InterfazPing):
    def __init__(self):
        self.ping = Ping()

    def ejecutar(self, direccion_ip):
        if direccion_ip == "192.168.0.254":
            self.ping.ejecutar_libre("www.google.com")
        else:
            self.ping.ejecutar(direccion_ip)

# Ejemplo de uso
if __name__ == "__main__":
    proxy = ProxyPing()
    proxy.ejecutar("192.168.0.1")
    print("=" * 30)
    proxy.ejecutar("8.8.8.8")
    print("=" * 30)
    proxy.ejecutar("192.168.0.254")
