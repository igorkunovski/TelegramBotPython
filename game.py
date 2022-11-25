# Программа для игры с конфетами бота против человека.

# Условие игры: На столе лежит 119 (число можно установить любое) конфет. Играют два игрока, делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
import commands
import random


total = 119
player = bool
insert = 0


def game(message):

    global total
    global player

    res = game_round()
    total -= res
    if total < 29:
        if not player:
            commands.bot.send_message(message.chat.id, f'Твоя взяла..!')
            commands.bot.send_message(message.chat.id, "/help - список мои команд")
            commands.bot.send_message(message.chat.id, "/game - игра")
            total = 119
            player = bool
            return
        else:
            commands.bot.send_message(message.chat.id, f'Я победил!')
            commands.bot.send_message(message.chat.id, "/help - список мои команд")
            commands.bot.send_message(message.chat.id, "/game - игра")
            total = 119
            player = bool
            return
    else:
        player = not player
        commands.bot.send_message(message.chat.id, f'-->Мой номер: {str(res)}')
        commands.bot.send_message(message.chat.id, f'***Всего остаток {str(total)}')
    return


def draw():
    # True - Human, False - computer
    return random.choice([True, False])


# # DUMP computer method
# def comp_play(total: int):
#     comp_num = random.randint(1, 28)
#     print(f'-->Computer number is:  {comp_num}')
#     return comp_num


# SMART Computer method - if starts, always wins
def comp_play():
    global total
    check_win = total - (total // 28 * 28) - 1
    if check_win >= 0:
        comp_num = check_win
    else:
        comp_num = random.randint(1, 28)
    return comp_num


def game_round():
    global player
    temp_total = insert if player else comp_play()
    return temp_total


def message_reply(message):
    global player
    global total
    global insert

    if "Y".upper() == message.text.upper():
        commands.bot.send_message(message.chat.id, "*** Игра начинается.***")
        player = draw()
        if not player:
            comp_plays = comp_play()
            commands.bot.send_message(message.chat.id, f' Мой ход {str(comp_plays)}')
            total -= comp_plays
            commands.bot.send_message(message.chat.id, f'Остаток {total}')
        else:
            commands.bot.send_message(message.chat.id, f' Число должно быть в пределе 1 - 28 ')

    elif message.text.isdigit() and 0 < int(message.text) < 29:

        commands.bot.send_message(message.chat.id, message.text)
        insert = int(message.text)
        total -= insert
        commands.bot.send_message(message.chat.id, f'Остаток {total}')
        game(message)

    elif message.text.isdigit() and (int(message.text) < 0 or int(message.text) > 28):
        commands.bot.send_message(message.chat.id, f'Число должно быть в пределе 1 - 28 ')
    else:
        inserted = message.text
        commands.bot.send_message(message.chat.id, inserted)
