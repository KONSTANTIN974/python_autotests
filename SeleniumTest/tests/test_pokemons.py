import requests
import pytest

URL ='https://api.pokemonbattle.ru/v2'
TOKEN ='9c9283af33e678a4b7bf117e95525f09'
HEADER ={'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '13358'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'ДиноЗоо'


@pytest.mark.parametrize('key, value', [('name', 'ДиноЗоо'), ('trainer_id', TRAINER_ID), ('id', '172366')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
