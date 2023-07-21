from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

import conf

bot = Bot(token=conf.token_key)  # создали эксземляр бота, с токеном
dp = Dispatcher(bot)  # инициализация диспетчера и передача экземпляра бота


@dp.message_handler()  # декоратор, обозначает событие, когда в чат, кто-то пишет
async def echo_send(message: types.Message):  # декорируемая асинхр функция,
                                                # сюда будут попадать события сообщений пользователей

    if message.text == 'Привет':
        await message.answer('Не пиши мне больше, педофил!')
    #await message.answer(message.text)  # ответ бота
    #await message.reply(message.text)  # бот будет упоминать сообщение, на которое отвечает
    #await bot.send_message(message.from_user.id, message.text)  # бот напишет польз в ЛС, но если польз уже писал боту
                                                                # message from user.id - айдишник пользователя

executor.start_polling(dp, skip_updates=True)  # запуск бота онлайн, передали диспетчера,
# skip_updates=True - бот не отвечает на сообщения, которые пришли, когда он был оффлайн

