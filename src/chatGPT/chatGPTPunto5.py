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
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

def main(api_key):
    """
    Función principal para ejecutar el programa.
    """
    # Inicializa la API de OpenAI con la clave proporcionada
    initialize_openai(api_key)
    
    # Inicializa variables para el modo conversación
    last_query = ""
    conversation_mode = False
    conversation_buffer = []

    try:
        # Loop principal del programa
        while True:
            try:
                usertask = " "
                context = ""

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
                            {"role": "system", "content": context},
                            {"role": "user", "content" : usertask},
                            {"role": "user", "content": userquery}
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
