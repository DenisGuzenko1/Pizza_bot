from aiogram import types, Dispatcher

from create_bot import bot,dp
from keyboards import kb_client
from data_base import sqlite_db
from keyboards.inline import inline_keyboard
from keyboards.inline import new_keyboard
from keyboards.inline import voting_keyboard
from aiogram.dispatcher.filters import Text
answ = dict()
# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Для общения с ботом в ЛС, напишите ему:\nhttps://t.me/Pizza_dini_bot')


# @dp.message_handler(commands=['Расписание'])
async def working_mode(message: types.Message):
    await bot.send_message(message.from_user.id, 'Мы работаем с 8.00 до 19.00')


# @dp.message_handler(commands=['Геолокация'])
async def location(message: types.Message):
    await bot.send_message(message.from_user.id, 'Мы на находимся на улице Победы, 9')

@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

async def url_commands(message: types.Message):  # инлайн кнопки с урлами
    await message.answer('Ссылочки', reply_markup=inline_keyboard)
async def new_inline(messsage: types.Message):  # хендляер который показывает инлай кнопку
    await messsage.answer('Ещё инлайн кнопки!', reply_markup=new_keyboard)

async def www_call(callback: types.CallbackQuery):  # когда мы нажмем на кнопку, ты всплывет окошко Инлайн кнопка нажата
    await callback.answer('Инлайн кнопка нажата',show_alert=True)  # если написать callback.message.answer, то бот в чат напишет \
    # иналайн кнопка нажата, но часики останутся, что бы это испр надо после callback.message.answer, написать\
    # callback.answer()


async def votice_butt(message: types.Message):
    await message.answer('ВЫборы выборы, кандидаты пидоры', reply_markup=voting_keyboard)


# @dp.callback_query_handler(Text(startswith='like_'))
async def votice(callback: types.CallbackQuery):
    res = int(callback.data.split(' ')[1])
    if callback.from_user.id not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(working_mode, commands=['Расписание'])
    dp.register_message_handler(location, commands=['Геолокация'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
    dp.register_message_handler(url_commands, commands=['ссылки'])
    dp.register_message_handler(new_inline, commands=['test'])
    dp.register_callback_query_handler(callback=www_call)
    dp.register_message_handler(votice_butt, commands=['голосование'])
    dp.register_callback_query_handler(callback=votice)
