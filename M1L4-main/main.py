import telebot 
from config import token
from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    username = message.from_user.username
    if username not in Pokemon.pokemons:
        pokemon = Pokemon(username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона!")

@bot.message_handler(commands=['levelup'])
def level_up(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        Pokemon.pokemons[username].level_up()
        bot.send_message(message.chat.id, f"Твой покемон теперь уровня {Pokemon.pokemons[username].level}")
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")

@bot.message_handler(commands=['info'])
def info(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        bot.send_message(message.chat.id, Pokemon.pokemons[username].info())
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")

bot.infinity_polling(none_stop=True)
