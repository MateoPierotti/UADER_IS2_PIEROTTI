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
        temperature=1,  # Temperatura para la generación del texto (1 es la configuración predeterminada)
        max_tokens=1000,  # Máximo número de tokens para generar la respuesta
        top_p=1,  # Probabilidad acumulativa máxima para elegir entre las palabras más probables
        frequency_penalty=0,  # Penalización de frecuencia para evitar la repetición de palabras
        presence_penalty=0  # Penalización de presencia para evitar la repetición de temas
    )

def process_user_input(conversation_buffer, last_query):
    """
    Procesa la entrada del usuario y retorna la consulta.
    """
    # Se crea el contexto utilizando las consultas anteriores del usuario, si existen
    context = " ".join([entry[0] for entry in conversation_buffer]) if conversation_buffer else ""
    
    # Se solicita al usuario ingresar una consulta
    print("Para iniciar el modo de conversación, escriba el siguiente comando en el terminal: python chatGPT.py --convers")
    print("Para salir del programa, ingrese la combinación de teclas 'Control + C'")
    userquery = input("Ingrese su consulta: ")

    # Se valida si la consulta del usuario está vacía y si no hay contexto, se lanza un error
    if userquery.strip() == "" and context.strip() == "":
        raise ValueError("Por favor, ingrese una consulta válida. (Complete todos los campos solicitados)")

    return userquery

def main(api_key):
    """
    Función principal para ejecutar el programa.
    """
    # Inicializa la API de OpenAI
    initialize_openai(api_key)
    
    last_query = ""  # Almacena la última consulta del usuario
    conversation_buffer = []  # Almacena las conversaciones anteriores del usuario

    try:
        while True:
            try:
                # Procesa la entrada del usuario y obtiene la consulta
                userquery = process_user_input(conversation_buffer, last_query)
            except ValueError as ve:
                print(f"Error en la aceptación de la consulta: {ve}")
            else:
                try:
                    # Invoca la API de OpenAI para obtener una respuesta
                    response = invoke_openai_api(
                        model="gpt-3.5-turbo-0125",
                        messages=[
                            {"role": "system", "content": " ".join([entry[0] for entry in conversation_buffer])},  # Contexto del sistema
                            {"role": "user", "content": userquery}  # Consulta del usuario
                        ]
                    )

                    # Imprime la consulta del usuario y la respuesta generada por OpenAI
                    print("Usuario: ", userquery)
                    print("chatGPT: ", response.choices[0].message.content)

                    # Almacena la conversación en el buffer
                    conversation_buffer.append((userquery, response.choices[0].message.content))

                except Exception as e:
                    print(f"Error durante la invocación de la API de OpenAI: {e}")

                last_query = userquery

    except KeyboardInterrupt:
        print("Programa terminado.")

if __name__ == "__main__":
    api_key = ""  # Aquí debes proporcionar tu propia clave API de OpenAI
    main(api_key)
