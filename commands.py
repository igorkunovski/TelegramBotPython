import emoji
import telebot
import _token
import calc_ration
import calc_complex


bot = telebot.TeleBot(_token.API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Возможные команды:")
    bot.send_message(message.chat.id, "/help - список мои команд")
    bot.send_message(message.chat.id, "/calc - калькулятор простых чисел")
    bot.send_message(message.chat.id, "/cplx - калькулятор комплексных чисел")
    bot.send_message(message.chat.id, "/game - игра ;)")


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, f'/help - список мои команд {emoji.emojize(":relaxed:")}')
    bot.send_message(message.chat.id, "/calc - калькулятор простых чисел")
    bot.send_message(message.chat.id, "/cplx - калькулятор комплексных чисел")
    bot.send_message(message.chat.id, "/game - игра ;)")


@bot.message_handler(commands=['calc'])
def calc_message(message):
    eq_list = message.text.split("/calc")
    if (len(eq_list) > 1) and eq_list[1] != "":
        expr = str(eq_list[1])
        result = calc_ration.simple_calc(expr)
        bot.send_message(message.chat.id, f'Это элементарно! {expr} = {result}')
    else:
        bot.send_message(message.chat.id, "необходимо ввести выражение в формате /calc 1+1")
        bot.send_message(message.chat.id, "Возможные символы для корректной работы + - / * ( )")


@bot.message_handler(commands=['cplx'])
def calc_complex_message(message):
    eq_list = message.text.split("/cplx")
    if (len(eq_list) > 1) and eq_list[1] != "":
        expr = str(eq_list[1])
        result = str(calc_complex.calc_complex(expr))
        bot.send_message(message.chat.id, f'Хмм.. {expr} = {result}')
    else:
        bot.send_message(message.chat.id, "необходимо ввести выражение в формате /cplx 1+1j")
        bot.send_message(message.chat.id, f'Возможные символы для корректной работы + - * / ( ) j')


@bot.message_handler(content_types='text')
def message_reply(message):
    if "привет".upper() in message.text.upper():
        bot.send_message(message.chat.id, 'и тебе ПРИВЕТ')
        bot.send_message(message.chat.id, "/help - список моих команд")
    else:
        bot.send_message(message.chat.id, "/help - список моих команд")


bot.polling()
