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
            cls._instance.banks_info = cls._instance._load_banks_info()
        return cls._instance

    def _load_banks_info(self):
        """
        Método para cargar la información de los bancos desde el archivo JSON.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as myfile:
                data = myfile.read()
            json_obj = json.loads(data)
            return json_obj.get("bancos", {})
        except FileNotFoundError:
            print(f"Error del programa: El archivo {self.file_path} no se encontró.")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Error del programa: El archivo no es un JSON válido.")
            sys.exit(1)

    def get_banks_info(self):
        """
        Método para obtener la información de los bancos.
        """
        return self.banks_info

class BankSelector:
    """
    Clase que implementa la selección automática de la cuenta bancaria.
    """
    def __init__(self, json_reader):
        """
        Constructor de la clase BankSelector.
        """
        self.json_reader = json_reader
        self.banks_info = self.json_reader.get_banks_info()

    def select_bank_account(self):
        """
        Método para seleccionar automáticamente la cuenta bancaria con mayor saldo.
        """
        try:
            banco_max_saldo = max(self.banks_info.values(), key=lambda x: x["saldo"])
            return banco_max_saldo["nombre"], banco_max_saldo["saldo"], banco_max_saldo["token"]
        except KeyError as e:
            print(f"Error: No se encontró la clave esperada en la información del banco: {e}")
            sys.exit(1)

    def get_bank_by_token(self, token):
        """
        Método para obtener la información de un banco específico basado en su token.
        """
        try:
            for bank in self.banks_info.values():
                if bank["token"] == token:
                    return bank["nombre"], bank["saldo"], bank["token"]
            print(f"Error: No se encontró ningún banco con el token '{token}'.")
            sys.exit(1)
        except KeyError as e:
            print(f"Error: No se encontró la clave esperada en la información del banco: {e}")
            sys.exit(1)

class Program:
    """
    Clase que representa el programa principal.
    """
    def __init__(self, bank_selector):
        """
        Constructor de la clase Program.
        """
        self.bank_selector = bank_selector

    def run(self, option, token=None):
        """
        Método principal que ejecuta el programa.
        """
        try:
            if option == "auto":
                # Selecciona automáticamente la cuenta bancaria con mayor saldo
                nombre_banco, saldo, token = self.bank_selector.select_bank_account()
                print(f"El banco con el mayor saldo es '{nombre_banco}' con un saldo de {saldo} y el token es {token}.")
            elif option == "token":
                if token is None:
                    print("Error: Se requiere un token para la opción 'token'.")
                    sys.exit(1)
                nombre_banco, saldo, token = self.bank_selector.get_bank_by_token(token)
                print(f"El banco con el token '{token}' es '{nombre_banco}' con un saldo de {saldo}.")
            else:
                print("Error: Opción no válida.")
                print_usage()
                sys.exit(1)
        except Exception as e:
            print(f"Error del programa: {e}")
            sys.exit(1)

def print_usage():
    """
    Función para imprimir el mensaje de uso del programa.
    """
    print("Uso: python programa.py <archivo_json> <opcion> [<token>]")
    print("Opciones:")
    print("  auto   - Seleccionar automáticamente el banco con mayor saldo.")
    print("  token  - Seleccionar un banco específico basado en su token.")
    print("Ejemplo: python programa.py archivo.json auto")
    print("Ejemplo: python programa.py archivo.json token ABCD1234")
    print("Para mostrar la versión del programa, ejecute: python programa.py -v")
    print("Para obtener ayuda, ejecute: python programa.py -h")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '-v':
        print(f"Versión del programa: {VERSION}")
        sys.exit(0)
    
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print_usage()
        sys.exit(0)

    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Error del programa: Número de argumentos inválido.")
        print_usage()
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    option = sys.argv[2]
    token = sys.argv[3] if len(sys.argv) == 4 else None

    try:
        json_reader = JSONReaderSingleton(json_file_path)
        bank_selector = BankSelector(json_reader)
        program = Program(bank_selector)
        program.run(option, token)
    except Exception as e:
        print(f"Error del programa: {e}")
        sys.exit(1)
