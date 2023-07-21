from aiogram.dispatcher import FSMContext  # мы указываем в хендлерах, что мы его исп в машине сост
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from create_bot import dp, bot
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_buttons

ID = None

class FSMadmin(StatesGroup):
    photo = State()  # запуск класса стэйт для обозначения состояния бота
    name = State()
    description = State()
    price = State()

# Получаем айди текущего модератора
@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID  #
    ID = message.from_user.id  #
    await bot.send_message(message.from_user.id, 'Что хозяин надо?!', reply_markup=admin_buttons.button_case_admin)  #
    await message.delete()
# Начало диалога загрузки нового пункта меню
#@dp.message_handler(commands='Загрузить', state=None)  # состояние нан т.к бот не нах в машине сост на момент старта

@dp.message_handler(state="*", commands='отмена')  # в каком бы состоянии польхователь не находился, * - люб состояние
@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")  # фильтр текта, кокой именно текст отменить
async def cancel_handler(message: types.Message, state: FSMContext):  #
    current_state = await state.get_state()  # получаем состояние бота
    if current_state is None:  # если бот не находится в состоянии
        return
    await state.finish()  # если состояние есть, то выходим из машины состояний
    await message.reply('OK')

async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMadmin.photo.set()  # как только написали загрузить, бот перейдет в режим машины сост и напиЗагрузи фото
        await message.reply('Загрузи фото')
# Ловим первый ответ и пишем в словарь
#@dp.register_message_handler(content_types=['photo'], state=FSMadmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:  # нам надо сохранить полученное фото в словарь
            data['photo'] = message.photo[0].file_id  # получаем айди файла и записываем в словарь
        await FSMadmin.next()  # переводим бота в режим ожидания следующего сообщения
        await message.reply('Теперь введи название')
# Ловим второй ответ
#@dp.register_message_handler(state=FSMadmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMadmin.next()
        await message.reply('Введи описание')
# Ловим третий ответ
#@dp.message_handler(state=FSMadmin.description)  #
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:  # лезем в словарь
            data['description'] = message.text  # записываем по ключу ссобщение админа
        await FSMadmin.next()  # переводим бота в следующее состояние
        await message.reply('Введи цену')
# Ловим 4 ответ и используем получение данных
#@dp.message_handler(state=FSMadmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)  # по ключу переводим в словарь сообщение админа
        #async with state.proxy() as data:
           # await message.reply(str(data))  # выведет после цены значения из спискав
        await sqlite_db.sql_add_command(state)
        await state.finish()  # завершаем состояние, выходим из машины состояний, очищаем словарь, поэтому\
    # работать с данными надо до этой команды


# Регистрируем хендлеры
def registr_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMadmin.photo)
    dp.register_message_handler(load_name, state=FSMadmin.name)
    dp.register_message_handler(load_description, state=FSMadmin.description)
    dp.register_message_handler(load_price, state=FSMadmin.price)
    dp.register_message_handler(make_changes_command,commands=['moderator'], is_chat_admin=True )