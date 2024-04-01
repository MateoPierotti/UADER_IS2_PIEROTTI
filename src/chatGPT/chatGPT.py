import openai
import pyreadline as readline

api_key = ""

openai.api_key = api_key

last_query = ""

try:
    try:
        usertask = ""
        context = ""    
        userquery = input("Ingrese su consulta: ")
        if userquery == "" and last_query:
            userquery = last_query
        if userquery.strip() == "" and usertask.strip() == "" and context.strip() == "" :
            raise ValueError("Por favor, ingrese una consulta válida. (Complete todos los campos solicitados)")
    except ValueError as ve:
        print(f"Error en la aceptación de la consulta: {ve}")
    else:
        try:   
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
            {
            "role": "system",
            # el contexto de operación
            "content": context },
            {
            "role": "user",
            # declaración de propósito
            "content" : usertask },
            {
            #la consulta
            "role": "user",
            "content": userquery }
            ],
            temperature=1,
            max_tokens=5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )

   
            print("You: ", userquery)
            
            print("chatGPT: ",response.choices[0].message.content)
        except Exception as e:
            print(f"Error durante la invocación de la API de OpenAI: {e}")
        last_query = userquery
except Exception as ex:
    print(f"Error general durante la ejecución del programa: {ex}")
