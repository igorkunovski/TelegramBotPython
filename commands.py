import telebot
import _token
import functions
import game

bot = telebot.TeleBot(_token.API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    functions.start_message(message)


@bot.message_handler(commands=['help'])
def help_message(message):
    functions.help_message(message)


@bot.message_handler(commands=['calc'])
def calc_message(message):
    functions.calc_message(message)


@bot.message_handler(commands=['cplx'])
def calc_complex_message(message):
    functions.calc_complex_message(message)


@bot.message_handler(commands=['game'])
def game_start_message(message):
    functions.game_start_message(message)


@bot.message_handler(content_types='text')
def message_reply(message):
    game.message_reply(message)


bot.polling()
