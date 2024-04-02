import openai
import sys

def initialize_openai(api_key):
    """
    Inicializa la API de OpenAI con la clave proporcionada.
    """
    openai.api_key = api_key

def invoke_openai_api(model, messages):
    """
    Invoca la API de OpenAI para obtener una respuesta.
    """
    return openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=1,  # Temperatura para la generación del texto (1 es la configuración predeterminada)
        max_tokens=1000,  # Máximo número de tokens para generar la respuesta
        top_p=1,  # Probabilidad acumulativa máxima para elegir entre las palabras más probables
        frequency_penalty=0,  # Penalización de frecuencia para evitar la repetición de palabras
        presence_penalty=0  # Penalización de presencia para evitar la repetición de temas
    )

def main(api_key):
    """
    Función principal para ejecutar el programa.
    """
    # Inicializa la API de OpenAI con la clave proporcionada
    initialize_openai(api_key)
    
    # Inicializa variables para el modo conversación
    last_query = ""  # Almacena la última consulta del usuario
    conversation_mode = False  # Indica si el modo conversación está activado
    conversation_buffer = []  # Almacena las conversaciones en modo conversación

    try:
        # Loop principal del programa
        while True:
            try:
                usertask = " "  # Tarea del usuario, no se utiliza actualmente
                context = ""  # Contexto de la conversación, se utiliza para mantener la coherencia en modo conversación

                # Si hay conversaciones anteriores en el buffer, se usa como contexto
                if conversation_buffer:
                    context = " ".join([entry[0] for entry in conversation_buffer])

                # Verifica si el modo conversación está activado
                if "--convers" in sys.argv:
                    conversation_mode = True
                    print("Modo conversación activado.")
                print("Para iniciar el modo de conversación, escriba el siguiente comando en el terminal: python chatGPT.py --convers")
                print("Para salir del programa, ingrese la combinación de teclas 'Control + C'")
                
                # Se solicita la consulta al usuario
                userquery = input("Ingrese su consulta: ")

                # Si estamos en modo conversación y no hay nueva consulta, se utiliza la anterior
                if conversation_mode and userquery == "" and last_query:
                    userquery = last_query

                # Si no se ingresa nada en la consulta, se muestra un mensaje de error
                if userquery.strip() == "" and usertask.strip() == "" and context.strip() == "":
                    raise ValueError("Por favor, ingrese una consulta válida. (Complete todos los campos solicitados)")
            except ValueError as ve:
                print(f"Error en la aceptación de la consulta: {ve}")
            else:
                try:
                    # Invoca la API de OpenAI para obtener la respuesta
                    response = invoke_openai_api(
                        model="gpt-3.5-turbo-0125",
                        messages=[
                            {"role": "system", "content": context},  # Contexto del sistema (conversaciones anteriores)
                            {"role": "user", "content" : usertask},  # Tarea del usuario (no utilizado actualmente)
                            {"role": "user", "content": userquery}  # Consulta del usuario
                        ]
                    )

                    # Imprime la consulta del usuario y la respuesta de chatGPT
                    print("Usuario: ", userquery)
                    print("chatGPT: ", response.choices[0].message.content)

                    # Si estamos en modo conversación, se agrega la conversación al buffer
                    if conversation_mode:
                        conversation_buffer.append((userquery, response.choices[0].message.content))

                except Exception as e:
                    print(f"Error durante la invocación de la API de OpenAI: {e}")

                # Actualiza la última consulta del usuario
                last_query = userquery

    except KeyboardInterrupt:
        print("Programa terminado.")

if __name__ == "__main__":
    api_key = ""
    main(api_key)
