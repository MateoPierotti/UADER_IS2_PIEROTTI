import openai
import pyreadline as readline  # Importa el módulo readline
import sys

# Define tu API key de OpenAI aquí
api_key = "tu_api_key_aqui"

# Configura la API key
openai.api_key = api_key

# Variable global para almacenar la última consulta y la conversación completa
last_query = ""
conversation_buffer = []

def main():
    global last_query, conversation_buffer  # Permite modificar las variables globales

    # Verifica si se proporcionó el argumento "--convers"
    if "--convers" in sys.argv:
        convers_mode = True
    else:
        convers_mode = False

    try:
        while True:  # Bucle para permitir recuperar la última consulta múltiples veces
            try:
                # Utiliza readline para leer la entrada del usuario
                print('Para salir del programa manualmente presione "Control + C"')
                user_query = input("Ingrese su consulta: ")
                

                # Verifica si se presionó la tecla "cursor Up" y estamos en modo conversación
                if convers_mode and user_query == "" and last_query:
                    user_query = last_query  # Utiliza la última consulta almacenada

            except KeyboardInterrupt:
                print("\nSe ha cancelado la entrada de datos.")
                return

            # Almacena la última consulta realizada en el buffer de conversación
            if user_query.strip() != "":
                conversation_buffer.append(user_query)

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
                    prompt="\n".join(conversation_buffer),
                    temperature=0.7,
                    max_tokens=150
                )

                # Imprime en pantalla la respuesta obtenida del API
                print("chatGPT:", response.choices[0].text.strip())

                # Agrega la respuesta de chatGPT al buffer de conversación para el modo "conversación"
                if convers_mode:
                    conversation_buffer.append(response.choices[0].text.strip())

            except Exception as e:
                # Maneja cualquier error que pueda ocurrir al invocar el API
                print("Ha ocurrido un error al invocar el API de OpenAI:", e)

            # Actualiza la última consulta realizada
            last_query = user_query

    except Exception as e:
        # Maneja cualquier otro error que pueda ocurrir en el programa
        print("Ha ocurrido un error:", e)

if __name__ == "__main__":
    main()
