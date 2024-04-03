"""
Este programa implementa un chatbot interactivo utilizando la API 
de OpenAI para generar respuestas basadas en la entrada del usuario.

El chatbot puede funcionar en dos modos:
1. Modo normal: El usuario ingresa una consulta y el chatbot responde.
2. Modo de conversación: El chatbot recuerda las consultas anteriores 
y las utiliza para contextualizar las respuestas en la conversación.

Para usar este programa, se necesita una clave de API de OpenAI válida.
"""
import sys
import openai

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
    initialize_openai(api_key)
    last_query = ""
    conversation_mode = False
    conversation_buffer = []

    try:
        while True:
            try:
                usertask = " "
                context = ""

                if conversation_buffer:
                    context = " ".join([entry[0] for entry in conversation_buffer])

                if "--convers" in sys.argv:
                    conversation_mode = True
                    print("Modo conversación activado.")
                print()
                print("para iniciar el modo de conversacion escriba")
                print("el siguiente codigo en el terminal: python chatGPT.py --convers")
                print("para salir del programa ingrese la combinacion de teclas 'Control + C'")
                print()
                userquery = input("Ingrese su consulta: ")

                if conversation_mode and userquery == "" and last_query:
                    userquery = last_query

                if userquery.strip() == "" and usertask.strip() == "" and context.strip() == "":
                    raise ValueError("Por favor, ingrese una consulta válida.")
            except ValueError as ve:
                print(f"Error en la aceptación de la consulta: {ve}")
            else:
                try:
                    response = invoke_openai_api(
                        model="gpt-3.5-turbo-0125",
                        messages=[
                            {"role": "system", "content": context},
                            {"role": "user", "content" : usertask},
                            {"role": "user", "content": userquery}
                        ]
                    )

                    print("You: ", userquery)
                    print("chatGPT: ", response.choices[0].message.content)

                    if conversation_mode:
                        conversation_buffer.append((userquery, response.choices[0].message.content))

                except openai.OpenAIError as e:
                    print(f"Error durante la invocación de la API de OpenAI: {e}")

                last_query = userquery

    except KeyboardInterrupt:
        print("Programa terminado.")

if __name__ == "__main__":
    OPENAI_API_KEY = ""
    main(OPENAI_API_KEY)
