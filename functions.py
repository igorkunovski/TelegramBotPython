import emoji
import calc_complex
import calc_ration
import commands


def start_message(message):
    commands.bot.send_message(message.chat.id, "Возможные команды:")
    commands.bot.send_message(message.chat.id, "/help - список мои команд")
    commands.bot.send_message(message.chat.id, "/calc - калькулятор простых чисел")
    commands.bot.send_message(message.chat.id, "/cplx - калькулятор комплексных чисел")
    commands.bot.send_message(message.chat.id, "/game - игра ;)")


def help_message(message):
    commands.bot.send_message(message.chat.id, f'/help - список мои команд {emoji.emojize(":relaxed:")}')
    commands.bot.send_message(message.chat.id, "/calc - калькулятор простых чисел")
    commands.bot.send_message(message.chat.id, "/cplx - калькулятор комплексных чисел")
    commands.bot.send_message(message.chat.id, "/game - игра ;)")


def calc_message(message):
    eq_list = message.text.split("/calc")
    if (len(eq_list) > 1) and eq_list[1] != "":
        expr = str(eq_list[1])
        result = calc_ration.simple_calc(expr)
        commands.bot.send_message(message.chat.id, f'Это элементарно! {expr} = {result}')
    else:
        commands.bot.send_message(message.chat.id, "необходимо ввести выражение в формате /calc 1+1")
        commands.bot.send_message(message.chat.id, "Возможные символы для корректной работы + - / * ( )")


def calc_complex_message(message):
    eq_list = message.text.split("/cplx")
    if (len(eq_list) > 1) and eq_list[1] != "":
        expr = str(eq_list[1])
        result = str(calc_complex.calc_complex(expr))
        commands.bot.send_message(message.chat.id, f'Хмм.. {expr} = {result}')
    else:
        commands.bot.send_message(message.chat.id, "необходимо ввести выражение в формате /cplx 1+1j")
        commands.bot.send_message(message.chat.id, f'Возможные символы для корректной работы + - * / ( ) j')


def message_reply(message):
    if "привет".upper() in message.text.upper():
        commands.bot.send_message(message.chat.id, 'и тебе ПРИВЕТ')
        commands.bot.send_message(message.chat.id, "/help - список моих команд")
    else:
        commands.bot.send_message(message.chat.id, "/help - список моих команд")