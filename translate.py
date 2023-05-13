import os
import openai
from redlines import Redlines
from IPython.display import display, Markdown, Latex, HTML, JSON
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # leer archivo .env local

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

prompt = f"""
Translate the following English text to Spanish: \ 
```Hi, I would like to order a blender```
"""
prompt2 = f"""
Tell me which language this is: 
```Combien coûte le lampadaire?```
"""
prompt3 = f"""
Translate the following  text to French and Spanish
and English pirate: \
```I want to order a basketball```
"""
prompt4 = f"""
Translate the following text to Spanish in both the \
formal and informal forms: 
'Would you like to order a pillow?'
"""

#Universal translator
user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                               # My screen is flashing
] 
# for issue in user_messages:
#     prompt = f"Tell me what language this is: ```{issue}```"
#     lang = get_completion(prompt)
#     print(f"Original message ({lang}): {issue}")

#     prompt5 = f"""
#     Translate the following  text to English \
#     and Korean: ```{issue}```
#     """

# Tone Transformation
prompt6 = f"""
Translate the following from slang to a business letter: 
'Dude, This is Joe, check out this spec on this standing lamp.'
"""
# Format Conversion
data_json = { "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

prompt7 = f"""
Translate the following python dictionary from JSON to an HTML \
table with column headers and title: {data_json}
"""
## Spellcheck/Grammar check.
text = [ 
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
  "Your going to need you’re notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for speling abilitty"  # spelling
]
for t in text:
    prompt8 = f"""Proofread and correct the following text
    and rewrite the corrected version. If you don't find
    and errors, just say "No errors found". Don't use 
    any punctuation around the text:
    ```{t}```"""
# corrector de texto mal escrito
text9 = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""
prompt9 = f"proofread and correct this review: ```{text9}```"

# otro
prompt10 = f"""
proofread and correct this review. Make it more compelling. 
Ensure it follows APA style guide and targets an advanced reader. 
Output in markdown format.
Text: ```{text9}```
"""
response = get_completion(prompt9)
print(response)

diff = Redlines(text9,response)
display(Markdown(diff.output_markdown))
# display(Markdown(response))