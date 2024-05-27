import json
import sys

VERSION = "versión 1.2"

class JSONReaderSingleton:
    """
    Clase que implementa un patrón Singleton para leer un archivo JSON.
    """
    def __new__(cls, file_path):
        """
        Método para crear una única instancia de la clase.
        """
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
            cls._instance.file_path = file_path
        return cls._instance

    def read_json(self):
        """
        Método para leer y cargar el contenido del archivo JSON.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as myfile:
                data = myfile.read()
            return json.loads(data)
        except FileNotFoundError:
            print(f"Error del programa: El archivo {self.file_path} no se encontró.")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Error del programa: El archivo no es un JSON válido.")
            sys.exit(1)

class JSONParser:
    """
    Clase que proporciona un método para parsear un objeto JSON y obtener información sobre los bancos.
    """
    @staticmethod
    def parse_json(json_obj):
        """
        Método para parsear un objeto JSON y obtener información sobre los bancos.
        """
        try:
            return json_obj["bancos"]
        except KeyError:
            print("Error del programa: No se encontró información sobre los bancos en el archivo JSON.")
            sys.exit(1)

class Program:
    """
    Clase que representa el programa principal.
    """
    def __init__(self, json_reader, json_parser):
        """
        Constructor de la clase Program.
        """
        self.json_reader = json_reader
        self.json_parser = json_parser

    def run(self):
        """
        Método principal que ejecuta el programa.
        """
        try:
            json_obj = self.json_reader.read_json()
            bancos_info = self.json_parser.parse_json(json_obj)
            banco_max_saldo = max(bancos_info.values(), key=lambda x: x["saldo"])
            nombre_banco_max_saldo = banco_max_saldo["nombre"]
            saldo_max_saldo = banco_max_saldo["saldo"]
            print(f"El banco con el mayor saldo es '{nombre_banco_max_saldo}' con un saldo de ${saldo_max_saldo} con este se realiza el pago.")
        except Exception as e:
            print(f"Error del programa: {e}")
            sys.exit(1)

def print_usage():
    """
    Función para imprimir el mensaje de uso del programa.
    """
    print("Uso: python programa.py <archivo_json>")
    print("Ejemplo: python programa.py archivo.json")
    print("Para mostrar la versión del programa, ejecute: python programa.py -v")
    print("Para obtener ayuda, ejecute: python programa.py -h")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '-v':
        print(f"Versión del programa: {VERSION}")
        sys.exit(0)
    
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print_usage()
        sys.exit(0)

    if len(sys.argv) != 2:
        print("Error del programa: Se requiere exactamente un argumento.")
        print_usage()
        sys.exit(1)
    
    json_file_path = sys.argv[1]

    try:
        json_reader = JSONReaderSingleton(json_file_path)
        json_parser = JSONParser()
        program = Program(json_reader, json_parser)
        program.run()
    except Exception as e:
        print(f"Error del programa: {e}")
        sys.exit(1)
