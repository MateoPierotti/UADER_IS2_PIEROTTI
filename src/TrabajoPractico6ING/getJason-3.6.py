import json, sys

def format_token(token):
    return f"{1.0}{token}"

if len(sys.argv) != 3 or sys.argv[1] == '-h':
    print("Para usar el programa ejecute el siguiente comando: {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json {clave}")
    sys.exit(1)

jsonfile = sys.argv[1]
jsonkey = sys.argv[2]

try:
    with open(jsonfile, "r") as myfile:
        data = myfile.read()
    obj = json.loads(data)
    print(format_token(str(obj[jsonkey])))
except FileNotFoundError:
    print(f"Error: El archivo {jsonfile} no se encontró.")
    sys.exit(1)
except KeyError:
    print(f"Error: La clave {jsonkey} no se encontró en el archivo JSON.")
    sys.exit(1)
except json.JSONDecodeError:
    print("Error: El archivo no es un JSON válido.")
    sys.exit(1)
except Exception as e:
    print(f"Error inesperado: {e}")
    sys.exit(1)
