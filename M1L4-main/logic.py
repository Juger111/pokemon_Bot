from random import randint
import requests

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(1, 1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.power = randint(30, 40)
        self.hp = randint(200, 400)
        self.level = 1  # Инициализация уровня
        Pokemon.pokemons[pokemon_trainer] = self

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['other']['official-artwork']['front_default']
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png"

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['forms'][0]['name']
        else:
            return "Pikachu"

    def level_up(self):
        self.level += 1
        self.power += 5

    def heal(self):
        self.hp = randint(200, 400)

    def info(self):
        return f"""Имя твоего покеомона: {self.name}
Уровень покемона: {self.level}
Сила покемона: {self.power}
Здоровье покемона: {self.hp}"""

    def show_img(self):
        return self.img

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1, 5)
            if chance == 1:
                return "🛡 Покемон-волшебник применил щит в сражении!"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"⚔️ Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}: нанесено {self.power} урона!"
        else:
            enemy.hp = 0
            return f"🏆 Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!"

class Wizard(Pokemon):
    def info(self):
        return '🧙 У тебя покемон-волшебник\n\n' + super().info()

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\n💥 Боец применил супер-атаку силой: {super_power}!"

    def info(self):
        return '🥊 У тебя покемон-боец\n\n' + super().info()


