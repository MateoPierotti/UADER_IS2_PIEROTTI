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

class TokenFormatter:
    """
    Clase que proporciona un método para formatear un token.
    """
    @staticmethod
    def format_token(token):
        """
        Método para formatear un token.
        """
        return f"{token}"

class JSONParser:
    """
    Clase que proporciona un método para parsear un objeto JSON y obtener un valor asociado a una clave.
    """
    @staticmethod
    def parse_json(json_obj, bank_name):
        """
        Método para parsear un objeto JSON y obtener un token asociado a un banco.
        """
        try:
            return json_obj["bancos"][bank_name]["token"]
        except KeyError:
            print(f"Error del programa: El banco '{bank_name}' no se encontró en el archivo JSON.")
            sys.exit(1)

class Program:
    """
    Clase que representa el programa principal.
    """
    def __init__(self, json_reader, token_formatter, json_parser):
        """
        Constructor de la clase Program.
        """
        self.json_reader = json_reader
        self.token_formatter = token_formatter
        self.json_parser = json_parser

    def run(self, bank_name):
        """
        Método principal que ejecuta el programa.
        """
        try:
            json_obj = self.json_reader.read_json()
            token = self.json_parser.parse_json(json_obj, bank_name)
            formatted_token = self.token_formatter.format_token(token)
            print(f"Token para el banco '{bank_name}': {formatted_token}")
        except Exception as e:
            print(f"Error del programa: {e}")
            sys.exit(1)

def print_usage():
    """
    Función para imprimir el mensaje de uso del programa.
    """
    print("Uso: python programa.py <archivo_json> <nombre_banco>")
    print("Ejemplo: python programa.py archivo.json BancoA")
    print("Para mostrar la versión del programa, ejecute: python programa.py -v")
    print("Para obtener ayuda, ejecute: python programa.py -h")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '-v':
        print(f"Versión del programa: {VERSION}")
        sys.exit(0)
    
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print_usage()
        sys.exit(0)

    if len(sys.argv) != 3:
        print("Error del programa: Se requieren exactamente dos argumentos.")
        print_usage()
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    bank_name = sys.argv[2]

    try:
        json_reader = JSONReaderSingleton(json_file_path)
        token_formatter = TokenFormatter()
        json_parser = JSONParser()
        program = Program(json_reader, token_formatter, json_parser)
        program.run(bank_name)
    except Exception as e:
        print(f"Error del programa: {e}")
        sys.exit(1)
