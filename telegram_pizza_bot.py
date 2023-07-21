from aiogram.utils import executor
from data_base import sqlite_db

from create_bot import dp


async def on_startup(_):
    print('Бот онлайн')  # функция, которая срабатывает при запуске бота, чтобы она зараб, надо её передать в executor
    sqlite_db.sql_start()

from handlers import client, other, admin

client.register_handlers_client(dp)
admin.registr_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # запуск бота онлайн, передали диспетчера,
# skip_updates=True - бот не отвечает на сообщения, которые пришли, когда он был офлайн
