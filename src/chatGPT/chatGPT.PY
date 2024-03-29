import openai
import pyreadline as readline  # Importa el módulo readline

# Define tu API key de OpenAI aquí
api_key = "tu_api_key_aqui"

# Configura la API key
openai.api_key = api_key

# Variable global para almacenar la última consulta
last_query = ""

def main():
    global last_query  # Permite modificar la variable global

    try:
        while True:  # Bucle para permitir recuperar la última consulta múltiples veces
            try:
                # Utiliza readline para leer la entrada del usuario
                user_query = input("Ingrese su consulta: ")

                # Verifica si se presionó la tecla "cursor Up"
                if user_query == "" and last_query:
                    user_query = last_query  # Utiliza la última consulta almacenada

            except KeyboardInterrupt:
                print("\nSe ha cancelado la entrada de datos.")
                return

            # Almacena la última consulta realizada
            last_query = user_query

            # Verifica si la consulta tiene texto
            if user_query.strip() == "":
                print("Por favor, ingrese una consulta válida.")
                continue

            # Imprime el contenido de la consulta con el prefijo "You:"
            print("You:", user_query)

            try:
                # Invoca el API de chatGPT con la consulta del usuario
                response = openai.Completion.create(
                    engine="text-davinci-003",  # Puedes cambiar el motor según tus necesidades
                    prompt=user_query,
                    temperature=0.7,
                    max_tokens=150
                )

                # Imprime en pantalla la respuesta obtenida del API
                print("chatGPT:", response.choices[0].text.strip())

            except Exception as e:
                # Maneja cualquier error que pueda ocurrir al invocar el API
                print("Ha ocurrido un error al invocar el API de OpenAI:", e)

    except Exception as e:
        # Maneja cualquier otro error que pueda ocurrir en el programa
        print("Ha ocurrido un error:", e)

if __name__ == "__main__":
    main()
