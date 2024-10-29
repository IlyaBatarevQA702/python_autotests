import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '731419db72ce9d1c1acec48e5a2c03f5'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}


body_create = {
    "name": "UFA",
    "photo_id": 2
}
body_change = {
    "pokemon_id": "118191",
    "name": "Ilya",
    "photo_id": 2
}
body_InPokeball = {
    "pokemon_id": "118191"
}


'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''Name_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(Name_change.text)'''

In_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_InPokeball)
print(In_pokeball.text)