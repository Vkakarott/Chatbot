import openai

API_KEY = "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" # Chave esta expirada

openai.api_key = API_KEY

def enviar_mens(mensagem, lista_mensagens = []):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )
    
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = lista_mensagens,
    )
    
    return response["choices"][0]["message"]

lista_mensagens = []
while True:
    txt = input("Escreva sua mensagem: ")
    
    if txt == "sair":
        print("Chatbot: Até logo!")
        break
    else:
        response = enviar_mens(txt, lista_mensagens)
        lista_mensagens.append(response)
        print("Chatbot: ", response["content"])