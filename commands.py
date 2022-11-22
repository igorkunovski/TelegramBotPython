import telebot
import _token
import functions


bot = telebot.TeleBot(_token.API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Возможные команды:")
    bot.send_message(message.chat.id, "/help - список мои команд")
    bot.send_message(message.chat.id, "/calc - калькулятор простых чисел")
    bot.send_message(message.chat.id, "/calc_complex - калькулятор комплексных чисел")
    bot.send_message(message.chat.id, "/game - игра ;)")


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, "/help - список мои команд")
    bot.send_message(message.chat.id, "/calc - калькулятор простых чисел")
    bot.send_message(message.chat.id, "/calc_complex - калькулятор комплексных чисел")
    bot.send_message(message.chat.id, "/game - игра ;)")


@bot.message_handler(commands=['calc'])
def calc_message(message):
    eq = message.text.split()[1:]
    bot.send_message(message.chat.id, f'calculated: {eval(eq[0])}')


@bot.message_handler(commands=['calc_complex'])
def start_message(message):
    bot.send_message(message.chat.id, "калькулирую")


@bot.message_handler(content_types='text')
def message_reply(message):
    if "привет".upper() in message.text.upper():
        bot.send_message(message.chat.id, 'и тебе ПРИВЕТ')
        bot.send_message(message.chat.id, "/help - список моих команд")
    else:
        bot.send_message(message.chat.id, "/help - список моих команд")


bot.polling()
