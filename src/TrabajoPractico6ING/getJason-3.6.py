import json
import sys

class JSONReaderSingleton:
    _instance = None

    def __new__(cls, file_path):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.file_path = file_path
        return cls._instance

    def read_json(self):
        try:
            with open(self.file_path, "r") as myfile:
                data = myfile.read()
            return json.loads(data)
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: El archivo {self.file_path} no se encontró.")
        except json.JSONDecodeError:
            raise ValueError("Error: El archivo no es un JSON válido.")

class TokenFormatter:
    @staticmethod
    def format_token(token):
        return f"{1.0}{token}"

class JSONParser:
    @staticmethod
    def parse_json(json_obj, key):
        try:
            return json_obj[key]
        except KeyError:
            raise KeyError(f"Error: La clave {key} no se encontró en el archivo JSON.")

class Program:
    def __init__(self, json_reader, token_formatter, json_parser):
        self.json_reader = json_reader
        self.token_formatter = token_formatter
        self.json_parser = json_parser

    def run(self, json_key):
        try:
            json_obj = self.json_reader.read_json()
            value = self.json_parser.parse_json(json_obj, json_key)
            formatted_token = self.token_formatter.format_token(str(value))
            print(formatted_token)
        except Exception as e:
            print(f"Error inesperado: {e}")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] == '-h':
        print("Para usar el programa ejecute el siguiente comando: {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json {clave}")
        sys.exit(1)
    
    json_file = sys.argv[1]
    json_key = sys.argv[2]

    json_reader = JSONReaderSingleton(json_file)
    token_formatter = TokenFormatter()
    json_parser = JSONParser()
    program = Program(json_reader, token_formatter, json_parser)
    program.run(json_key)
