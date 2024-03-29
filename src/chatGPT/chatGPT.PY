import openai

# Define tu API key de OpenAI aquí
api_key = "tu_api_key_aqui"

# Configura la API key
openai.api_key = api_key

def main():
    # Acepta una consulta del usuario
    user_query = input("Ingrese su consulta: ")

    # Verifica si la consulta tiene texto
    if user_query.strip() == "":
        print("Por favor, ingrese una consulta válida.")
        return

    # Imprime el contenido de la consulta con el prefijo "You:"
    print("You:", user_query)

    # Invoca el API de chatGPT con la consulta del usuario
    response = openai.Completion.create(
        engine="text-davinci-003",  # Puedes cambiar el motor según tus necesidades
        prompt=user_query,
        temperature=0.7,
        max_tokens=150
    )

    # Imprime en pantalla la respuesta obtenida del API
    print("chatGPT:", response.choices[0].text.strip())

if __name__ == "__main__":
    main()
