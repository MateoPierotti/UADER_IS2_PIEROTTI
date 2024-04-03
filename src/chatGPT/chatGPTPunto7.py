"""
    Este codigo es brindado por chatGPT implementando mejoras
"""
import sys
import openai
import argparse

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

def main(api_key, conversation_mode):
    """
    Función principal para ejecutar el programa.
    """
    initialize_openai(api_key)
    last_query = ""
    conversation_buffer = []

    try:
        while True:
            try:
                if conversation_buffer:
                    context = " ".join([entry[0] for entry in conversation_buffer])
                else:
                    context = ""

                if conversation_mode and last_query:
                    userquery = last_query
                else:
                    userquery = input("You: ")

                if not userquery.strip():
                    raise ValueError("Por favor, ingrese una consulta válida.")
            except ValueError as ve:
                print(f"Error: {ve}")
            else:
                try:
                    response = invoke_openai_api(
                        model="gpt-3.5-turbo-0125",
                        messages=[
                            {"role": "system", "content": context},
                            {"role": "user", "content": userquery}
                        ]
                    )

                    print("chatGPT: ", response.choices[0].message.content)

                    if conversation_mode:
                        conversation_buffer.append((userquery, response.choices[0].message.content))

                except openai.OpenAIError as e:
                    print(f"Error: {e}")

                last_query = userquery

    except KeyboardInterrupt:
        print("Programa terminado.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chatbot interactivo usando la API de OpenAI")
    parser.add_argument("--convers", action="store_true", help="Activar modo conversación")
    args = parser.parse_args()

    OPENAI_API_KEY = ""
    main(OPENAI_API_KEY, args.convers)
