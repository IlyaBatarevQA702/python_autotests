import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '731419db72ce9d1c1acec48e5a2c03f5'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}
TRAINER_ID = 7672

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_trainer_id():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Ilya'
    print(response_get.text)