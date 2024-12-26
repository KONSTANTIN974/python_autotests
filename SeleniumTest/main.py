import requests 
URL ='https://api.pokemonbattle.ru/v2'
TOKEN ='9c9283af33e678a4b7bf117e95525f09'
HEADER ={'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_registration ={
    "trainer_token": TOKEN,
    "email": "orl.constantin@yandex.ru",
    "password": "Iloveqa1"
}
body_confirmation = {
    "trainer_token" : TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

response = requests.post(url = f'{URL}/trainers/reg', headers=HEADER, json=body_registration )
print(response.text)

response_confirmation = requests.post(url=f'{URL}/trainers/confirm_email', headers= HEADER, json=body_confirmation)
print(response_confirmation.text)

response_create = requests.post(url=f'{URL}/pokemons', headers= HEADER, json = body_create )
print(response_create.text)

message = response_create.json()['message']
print(message)


response = requests.put(url=f'{URL}/pokemons',
                         json={
                            "pokemon_id": "172366",
                            "name": "Динозоо1",
                            "photo_id": 2},
                            headers={"Content-Type":"application/json", "trainer_token": TOKEN}
                        )
print(response.text)


response = requests.post(url=f'{URL}/trainers/add_pokeball',
                         json={
                          "pokemon_id": "98379"},
                            headers={"Content-Type":"application/json", "trainer_token": TOKEN})
print(response.text)
