# Importar las bibliotecas necesarias
import os
import openai
from dotenv import load_dotenv, find_dotenv

# Carga el archivo .env que contiene la clave de la API de OpenAI
_ = load_dotenv(find_dotenv())

# Configura la clave de la API de OpenAI a partir de la variable de entorno
openai.api_key = os.getenv('OPENAI_API_KEY')

# Esta función realiza una solicitud de finalización de chat a la API de OpenAI con una lista de mensajes
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    # Hacer la llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model=model,  # especifica el modelo a utilizar
        messages=messages,  # proporciona los mensajes
        temperature=temperature,  # define el grado de aleatoriedad de la salida del modelo
    )
    
    # Imprime el mensaje generado por el modelo
    print(str(response.choices[0].message))
    
    # Devuelve el contenido del mensaje generado por el modelo
    return response.choices[0].message["content"]

messages =  [  
{'role':'system', 'content':'You are friendly chatbot.'},
{'role':'user', 'content':'Hi, my name is Isa'},
{'role':'assistant', 'content': "Hi Isa! It's nice to meet you. \
Is there anything I can help you with today?"},
{'role':'user', 'content':'Yes, you can remind me, What is my name?'}  ]
response = get_completion_from_messages(messages, temperature=1)
print(response)

# assistant: El rol del asistente representa al propio chatbot. Estos mensajes son respuestas previas del chatbot en la conversación. 
# Al incluir las respuestas anteriores del asistente, se ayuda al modelo a mantener la coherencia y el contexto durante la conversación.