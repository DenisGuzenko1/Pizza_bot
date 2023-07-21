import json
import string

from aiogram import types, Dispatcher


# @dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('maty.json')))) != set():
        await message.reply('Хули материшся, еблан')
        await message.delete()
        # если в сообщении есть мат, который пересекается с матом с json файла, то множеств не путст и срабатывает код


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
