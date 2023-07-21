from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # для создания хранилища состояний
from aiogram.dispatcher import Dispatcher

import conf

storage = MemoryStorage()
bot = Bot(token=conf.token_key)
dp = Dispatcher(bot, storage=storage)  # передали хранилище в диспетчер
