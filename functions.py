import emoji
import calc_complex
import calc_ration
import commands


def start_message(message):
    commands.bot.send_message(message.chat.id, "Возможные команды:")
    commands.bot.send_message(message.chat.id, "/help - список мои команд")
    commands.bot.send_message(message.chat.id, "/calc - калькулятор простых чисел")
    commands.bot.send_message(message.chat.id, "/cplx - калькулятор комплексных чисел")
    commands.bot.send_message(message.chat.id, "/game - игра")


def help_message(message):
    commands.bot.send_message(message.chat.id, f'/help - список мои команд {emoji.emojize(":woozy_face:")}')
    commands.bot.send_message(message.chat.id, f'/calc - калькулятор простых чисел {emoji.emojize(":abacus:")}')
    commands.bot.send_message(message.chat.id, f'/cplx - калькулятор комплексных чисел'
                                               f' {emoji.emojize(":confused_face:")}{emoji.emojize(":abacus:")}')
    commands.bot.send_message(message.chat.id, f'/game - игра {emoji.emojize(":game_die:")}')


def calc_message(message):
    eq_list = message.text.split("/calc")
    if (len(eq_list) > 1) and eq_list[1] != "":
        expr = str(eq_list[1])
        result = calc_ration.simple_calc(expr)
        commands.bot.send_message(message.chat.id, f'Это элементарно!{emoji.emojize(":nerd_face:")} {expr} = {result}')
    else:
        commands.bot.send_message(message.chat.id, "необходимо ввести выражение в формате /calc 1+1")
        commands.bot.send_message(message.chat.id, "Возможные символы для корректной работы + - / * ( )")


def calc_complex_message(message):
    eq_list = message.text.split("/cplx")
    if (len(eq_list) > 1) and eq_list[1] != "":
        expr = str(eq_list[1])
        result = str(calc_complex.calc_complex(expr))
        commands.bot.send_message(message.chat.id, f'Хмм..{emoji.emojize(":face_with_rolling_eyes:")} {expr} = {result}')
    else:
        commands.bot.send_message(message.chat.id, "необходимо ввести выражение в формате /cplx 1+1j")
        commands.bot.send_message(message.chat.id, f'Возможные символы для корректной работы + - * / ( ) j')


def game_start_message(message):
    commands.bot.send_message(message.chat.id, "Условие игры: На столе лежит 119 конфет. Играют два игрока делая "
                                               "ход друг после друга. Первый ход определяется жеребьёвкой. За один "
                                               "ход можно забрать не более чем 28 конфет. Все конфеты оппонента "
                                               "достаются сделавшему последний ход.")
    commands.bot.send_message(message.chat.id, "Для старта и жеребъевки первого хода нажми Y ")
