import string

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import json
import os
import string

import conf

bot = Bot(token=conf.token_key)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот онлайн')  # функция, которая срабатывает при запуске бота, чтобы она зараб, надо её передать в executor

'''***********************************************КЛИЕНТСКАЯ ЧАСТЬ***************************************************'''
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('Для общения с ботом в ЛС, напишите ему:\nhttps://t.me/Pizza_dini_bot')
@dp.message_handler(commands=['Расписание'])
async def working_mode(message: types.Message):
    await bot.send_message(message.from_user.id,'Мы работаем с 8.00 до 19.00')

@dp.message_handler(commands=['Геолокация'])
async def location(message: types.Message):
    await bot.send_message(message.from_user.id, 'Мы на находимся на улице Победы, 9')

'''***********************************************АДМИНСКАЯ ЧАСТЬ****************************************************'''

'''***********************************************ОБЩАЯ ЧАСТЬ********************************************************'''

@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('maty.json')))) != set():
        await message.reply('Хули материшся, еблан')
        await message.delete()
        # если в сообщении есть мат, который пересекается с матом с json файла, то множеств не путст и срабатывает код


executor.start_polling(dp, skip_updates=True, on_startup= on_startup)  # запуск бота онлайн, передали диспетчера,
# skip_updates=True - бот не отвечает на сообщения, которые пришли, когда он был офлайн

