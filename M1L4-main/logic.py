from random import randint
import requests

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1, 1000)
        self.level = randint(1, 10)

        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.name = data['forms'][0]['name']
            self.img = data['sprites']['front_default']
            self.height = data['height']
            self.weight = data['weight']
            self.types = [t['type']['name'] for t in data['types']]
        else:
            self.name = "pikachu"
            self.img = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
            self.height = 4
            self.weight = 60
            self.types = ['electric']

        Pokemon.pokemons[pokemon_trainer] = self

    def info(self):
        return (
            f"Имя: {self.name}\n"
            f"Уровень: {self.level}\n"
            f"Типы: {', '.join(self.types)}\n"
            f"Рост: {self.height}\n"
            f"Вес: {self.weight}"
        )

    def show_img(self):
        return self.img

    def level_up(self):
        self.level += 1
