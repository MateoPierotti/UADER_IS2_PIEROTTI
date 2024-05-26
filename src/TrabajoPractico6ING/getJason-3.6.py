"""
Este programa permite leer un archivo JSON y extraer un valor asociado a una clave.
Es propiedad de la compañía UADERFCyT-IS2©2024, todos los derechos reservados.
"""

import json
import sys

class JSONReaderSingleton:
    """
    Clase que implementa un patrón Singleton para leer un archivo JSON.
    """
    _instance = None

    def __new__(cls, file_path):
        """
        Método para crear una única instancia de la clase.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.file_path = file_path
        return cls._instance

    def read_json(self):
        """
        Método para leer y cargar el contenido del archivo JSON.
        """
        try:
            with open(self.file_path, "r") as myfile:
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
        return f"{1.0}{token}"

class JSONParser:
    """
    Clase que proporciona un método para parsear un objeto JSON y obtener un valor asociado a una clave.
    """
    @staticmethod
    def parse_json(json_obj, key):
        """
        Método para parsear un objeto JSON y obtener un valor asociado a una clave.
        """
        try:
            return json_obj[key]
        except KeyError:
            print(f"Error del programa: La clave {key} no se encontró en el archivo JSON.")
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

    def run(self, json_key):
        """
        Método principal que ejecuta el programa.
        """
        try:
            json_obj = self.json_reader.read_json()
            value = self.json_parser.parse_json(json_obj, json_key)
            formatted_token = self.token_formatter.format_token(str(value))
            print(formatted_token)
        except Exception as e:
            print(f"Error del programa: {e}")
            sys.exit(1)

def print_usage():
    """
    Función para imprimir el mensaje de uso del programa.
    """
    print("Uso: python programa.py <archivo_json> <clave>")
    print("Ejemplo: python programa.py archivo.json clave")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error del programa: Se requieren exactamente dos argumentos.")
        print_usage()
        sys.exit(1)
    
    if sys.argv[1] == '-h':
        print_usage()
        sys.exit(0)
    
    json_file = sys.argv[1]
    json_key = sys.argv[2]

    try:
        json_reader = JSONReaderSingleton(json_file)
        token_formatter = TokenFormatter()
        json_parser = JSONParser()
        program = Program(json_reader, token_formatter, json_parser)
        program.run(json_key)
    except Exception as e:
        print(f"Error del programa: {e}")
        sys.exit(1)
