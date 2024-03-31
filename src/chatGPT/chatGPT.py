import openai
api_key = ""

openai.api_key = api_key

usertask = input("Ingrese el propósito de su consulta: ")
context = input("Ingrese el contexto de su consulta: ")
userquery = input("Ingrese su consulta: ")
if userquery.strip() == "" and usertask.strip() == "" and context.strip() == "" :
    print("Por favor, ingrese una consulta válida. (Complete todos los campos solicitados)")
else:   
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
    # Concatenar las variables en una sola cadena
    consulta_completa = f"Propósito: {usertask} Contexto: {context} Consulta: {userquery}"

    # Imprimir la consulta completa
    print("You: ", consulta_completa)
    print("chatGPT: ",response.choices[0].message.content)