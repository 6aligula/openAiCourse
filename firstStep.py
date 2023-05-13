import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # leer archivo .env local

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt1, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt1}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # este es el grado de aleatoriedad de la salida del modelo
    )
    return response.choices[0].message["content"]
# ejemplo 1
texto = f"""
Deberías expresar lo que quieres que un modelo haga proporcionando \
instrucciones que sean lo más claras y específicas posibles. \
Esto guiará al modelo hacia la salida deseada, reduciendo las \
posibilidades de recibir respuestas irrelevantes o incorrectas. \
No confundas escribir un prompt claro con escribir un prompt corto. \
En muchos casos, los prompts más largos proporcionan más claridad y \
contexto para el modelo, lo que puede llevar a salidas más detalladas \
y relevantes.
"""
prompt = f"""
Resumir el texto delimitado por comillas invertidas triples \
en una sola oración.
```{texto}```
"""
# ejemplo 2
prompt1 = f"""
Genera una lista de tres títulos de libros inventados junto con \
sus autores y géneros. Proporciónalos en formato JSON con las siguientes claves: 
book_id, title, author, genre.
"""
# ejemplo 3
texto_1 = f"""
¡Hacer una taza de té es fácil! Primero, necesitas hervir un poco de \
agua. Mientras eso sucede, toma una taza y coloca una bolsa de té en ella. \
Una vez que el agua esté suficientemente caliente, simplemente viértela sobre la bolsa de té. \
Deja reposar un poco para que el té pueda infusionarse. Después de unos \
minutos, saca la bolsa de té. Si te gusta, puedes agregar un poco de azúcar o leche al gusto. \
¡Y eso es todo! Tienes una deliciosa taza de té para disfrutar.
"""
prompt_1 = f"""
Se te proporcionará un texto delimitado por comillas triples. \
Si contiene una secuencia de instrucciones, reescribe esas instrucciones en el siguiente formato:

Paso 1 - ...
Paso 2 - …
…
Paso N - …

Si el texto no contiene una secuencia de instrucciones, \
entonces simplemente escribe \"No se proporcionaron pasos.\"

\"\"\"{texto_1}\"\"\"
"""
# ejemplo 4
prompt_few_shot = f"""
Tu tarea es responder en un estilo consistente.

<niño>: Enséñame sobre la paciencia.

<abuelo>: El río que talla el valle más profundo fluye de una fuente modesta; la \
sinfonía más grandiosa se origina a partir de una sola nota; \
el tapiz más intrincado comienza con un solo hilo.

<niño>: Enséñame sobre la resiliencia.
"""
# ejemplo 5
texto_think = f"""
En un encantador pueblo, los hermanos Jack y Jill emprendieron \
una misión para buscar agua de un pozo en la cima de una colina. \
Mientras subían, cantando alegremente, la desgracia golpeó: Jack tropezó \
con una piedra y rodó colina abajo, seguido por Jill. \
Aunque ligeramente maltratados, la pareja regresó a casa para recibir \
abrazos reconfortantes. A pesar del percance, su espíritu aventurero \
permaneció inalterado y continuaron explorando con deleite.
"""
prompt_think = f"""
Realiza las siguientes acciones: 
1 - Resume el siguiente texto delimitado por comillas triples \
con 1 oración.
2 - Traduce el resumen al francés.
3 - Enumera cada nombre en el resumen en francés.
4 - Genera un objeto json que contenga las siguientes \
claves: resumen_frances, num_nombres.

Separa tus respuestas con saltos de línea.

Texto:
```{texto_think}```
"""
#ejemplo 6
prompt_6 = f"""
Tu tarea es realizar las siguientes acciones: 
1 - Resume el siguiente texto delimitado por 
  <> con 1 frase.
2 - Traduce el resumen al francés.
3 - Enumera cada nombre en el resumen en francés.
4 - Genera un objeto json que contenga las 
  siguientes claves: resumen_frances, num_nombres.

Usa el siguiente formato:
Texto: <texto a resumir>
Resumen: <resumen>
Traducción: <traducción del resumen>
Nombres: <lista de nombres en el resumen en francés>
JSON de salida: <json con el resumen y num_nombres>

Texto: <{texto_think}>
"""
# ejemplo 7
prompt_7 = f"""
Determina si la solución del estudiante es correcta o no.\
is correct or not.
To solve the problem do the following:
- First, work out your own solution to the problem. 
- Then compare your solution to the student's solution \ 
and evaluate if the student's solution is correct or not. 
Don't decide if the student's solution is correct until 
you have done the problem yourself.

Use the following format:
Question:
```
question here
```
Student's solution:
```
student's solution here
```
Actual solution:
```
steps to work out the solution and your solution here
```
Is the student's solution the same as actual solution \
just calculated:
```
yes or no
```
Student grade:
```
correct or incorrect
```
Pregunta:
Estoy construyendo una instalación de energía solar y necesito \
ayuda para calcular los costos. 
- El terreno cuesta $100 por pie cuadrado
- Puedo comprar paneles solares por $250 por pie cuadrado
- Negocié un contrato de mantenimiento que me costará \
un fijo de $100k por año, y un adicional de $10 por pie \
cuadrado
¿Cuál es el costo total para el primer año de operaciones 
como función del número de pies cuadrados?

Solución del estudiante:
Dejemos que x sea el tamaño de la instalación en pies cuadrados.
Costos:
1. Costo del terreno: 100x
2. Costo de los paneles solares: 250x
3. Costo de mantenimiento: 100,000 + 100x
Costo total: 100x + 250x + 100,000 + 100x = 450x + 100,000
"""


response = get_completion(prompt_7)
print(response)
