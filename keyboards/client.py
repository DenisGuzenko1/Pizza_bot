from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Расписание')
b2 = KeyboardButton('/Геолокация')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('Поделиться номером', request_contact=True)  # служебные кнопки(отправит контакт в бота)
b5 = KeyboardButton('Отправить где я,', request_location=True)  # отправит геолокацию пользователя

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).insert(b2).add(b3).insert(b4).add(b5)  # метод add добавляет кнопку каждый раз с новой строки
