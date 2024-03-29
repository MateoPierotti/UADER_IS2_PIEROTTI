import openai

api_key = "tu_api_key_aqui"

openai.api_key = api_key

def main():
    try:
        # Acepta una consulta del usuario
        try:
            user_query = input("Ingrese su consulta: ")
        except KeyboardInterrupt:
            print("\nSe ha cancelado la entrada de datos.")
            return

        # Verifica si la consulta tiene texto
        if user_query.strip() == "":
            print("Por favor, ingrese una consulta válida.")
            return

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
