import telebot
from config import token
from logic import Pokemon, Wizard, Fighter

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id,
        "/go - создать обычного покемона\n"
        "/wizard - создать покемона-волшебника\n"
        "/fighter - создать покемона-бойца\n"
        "/info - информация о покемоне\n"
        "/levelup - повысить уровень\n"
        "/heal - восстановить здоровье\n"
        "/attack @username - атаковать другого покемона"
    )

@bot.message_handler(commands=['go'])
def go(message):
    username = message.from_user.username
    if username not in Pokemon.pokemons:
        pokemon = Pokemon(username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона!")

@bot.message_handler(commands=['wizard'])
def create_wizard(message):
    username = message.from_user.username
    if username not in Pokemon.pokemons:
        pokemon = Wizard(username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона!")

@bot.message_handler(commands=['fighter'])
def create_fighter(message):
    username = message.from_user.username
    if username not in Pokemon.pokemons:
        pokemon = Fighter(username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона!")

@bot.message_handler(commands=['info'])
def info(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        bot.send_message(message.chat.id, Pokemon.pokemons[username].info())
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")

@bot.message_handler(commands=['levelup'])
def level_up(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[username]
        pokemon.level_up()
        bot.send_message(message.chat.id,
            f"🔼 Твой покемон теперь уровня {pokemon.level} и сила {pokemon.power}"
        )
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")

@bot.message_handler(commands=['attack'])
def attack(message):
    username = message.from_user.username
    args = message.text.split()

    if len(args) != 2:
        bot.reply_to(message, "Используй команду так: /attack @имя_врага")
        return

    enemy_name = args[1].lstrip('@')

    if username not in Pokemon.pokemons:
        bot.reply_to(message, "Сначала создай покемона командой /go")
        return
    if enemy_name not in Pokemon.pokemons:
        bot.reply_to(message, "У противника нет покемона.")
        return

    my_pokemon = Pokemon.pokemons[username]
    enemy_pokemon = Pokemon.pokemons[enemy_name]

    result = my_pokemon.attack(enemy_pokemon)
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['feed'])
def feed_pok(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        result = Pokemon.pokemons[username].feed()
        bot.send_message(message.chat.id, result)
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")
bot.infinity_polling(none_stop=True)
