import os
import openai
from dotenv import load_dotenv, find_dotenv
import panel as pn  # GUI
pn.extension()

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

# Esta función actualiza la conversación en la GUI cada vez que se envía un mensaje del usuario
def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('Usuario:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Asistente:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
    
    # Añade el resumen en formato JSON del pedido de comida anterior
    messages = context.copy()
    messages.append(
    {'role':'system', 'content':'create a json summary of the previous food order. Itemize the price for each item\
    The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, include size   4) list of sides include size  5)total price '},    
    )
    
    response = get_completion_from_messages(messages, temperature=0)
    print(response)
    
    return pn.Column(*panels)


panels = []  # almacena los elementos de la conversación en la GUI

# Establece el contexto inicial para el modelo de lenguaje
context = [ {'role':'system', 'content':"""
Eres OrderBot, un servicio automatizado para recoger pedidos para un restaurante de pizzas. \
Primero saludas al cliente, luego recopilas el pedido, \
y luego preguntas si es para recoger o para entregar. \
Esperas para recopilar todo el pedido, luego lo resumen y verifican por última \
vez si el cliente desea agregar algo más. \
Si es una entrega, pide una dirección. \
Finalmente, recopilas el pago. \
Asegúrate de aclarar todas las opciones, extras y tamaños para identificar de manera única \
el artículo del menú. \
Responde en un estilo amigable, breve y muy conversacional. \
El menú incluye \
pizza de pepperoni 12.95, 10.00, 7.00 \
pizza de queso 10.95, 9.25, 6.50 \
pizza de berenjena 11.95, 9.75, 6.75 \
papas fritas 4.50, 3.50 \
ensalada griega 7.25 \
Ingredientes adicionales: \
queso extra 2.00, \
champiñones 1.50 \
salchicha 3.00 \
jamón canadiense 3.50 \
salsa AI 1.50 \
pimientos 1.00 \
Bebidas: \
coca-cola 3.00, 2.00, 1.00 \
sprite 3.00, 2.00, 1.00 \
agua embotellada 5.00 \
"""} ]  # acumula mensajes


# Configura los widgets de Panel para la entrada de texto y el botón de chat
inp = pn.widgets.TextInput(value="Hola", placeholder='Escribe aquí…')
button_conversation = pn.widgets.Button(name="¡Chatear!")

# Vincula la función collect_messages al botón de chat
interactive_conversation = pn.bind(collect_messages, button_conversation)

# Crea el diseño del panel para la GUI del chat
dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

# Inicia el servidor de Panel y muestra la GUI en el navegador
pn.serve(dashboard)
