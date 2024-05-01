import requests

api_key = 'e1904178-0be7-4fef-b430-62b64af54cb4'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
res = requests.get(url)
definitions = res.json()
for definitions in definitions:
    print(definitions)