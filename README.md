# Chatbot com OpenAI GPT-3.5

Este projeto implementa um chatbot utilizando a API da OpenAI para interagir com o modelo GPT-3.5. O chatbot recebe mensagens do usuário e responde de acordo utilizando o modelo `gpt-3.5-turbo`.

## Estrutura do Código

### `import openai`
Importa a biblioteca da OpenAI para interagir com a API.

### `API_KEY`
A chave de API usada para autenticar as solicitações à OpenAI.

### `openai.api_key = API_KEY`
Configura a chave de API para o uso no código.

### Função `enviar_mens`
Esta função recebe uma mensagem e uma lista de mensagens anteriores, então envia uma solicitação à API da OpenAI e retorna a resposta.

#### Parâmetros:
- `mensagem` (string): A mensagem enviada pelo usuário.
- `lista_mensagens` (list): A lista de mensagens anteriores no formato esperado pela API. Essa lista é atualizada a cada interação.

#### Retorno:
- Retorna a mensagem de resposta gerada pelo modelo.

### Loop Principal
O código principal do programa roda em um loop que:
- Recebe a entrada do usuário.
- Envia a mensagem para a função `enviar_mens`.
- Exibe a resposta gerada pelo modelo.
- O loop continua até que o usuário digite "sair".

## Requisitos

- Python 3.x
- Biblioteca `openai` instalada: Você pode instalar a biblioteca utilizando o comando `pip install openai`.

## Como Usar

1. Clone o repositório ou copie o código para um arquivo Python.
2. Substitua `API_KEY` pela sua chave da API da OpenAI.
3. Execute o script e comece a interagir com o chatbot.

## Observação

Lembre-se de que a chave de API no código é fictícia e deve ser substituída pela sua chave real da OpenAI. **Nunca compartilhe sua chave de API publicamente**.
