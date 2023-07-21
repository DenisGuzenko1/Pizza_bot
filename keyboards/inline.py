from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from conf import token_key
from create_bot import dp, bot

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard = InlineKeyboardMarkup(row_width=1)
first_button = InlineKeyboardButton(text='Ссылка',
                                    url='https://www.youtube.com/watch?v=gpCIfQUbYlY&list=PLNi5HdK6QEmX1OpHj0wvf8Z28NYoV5sBJ&index=9')
second_button = InlineKeyboardButton(text='Ссылка 2', url='https://pass.rw.by/ru/')
inline_keyboard.add(first_button, second_button)

new_keyboard = InlineKeyboardMarkup(row_width=1)
first_call_butt = InlineKeyboardButton(text='Нажми меня', callback_data='www')  # нажми меня будет написано на кнопке
new_keyboard.add(first_call_butt)

voting_keyboard = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Like', callback_data='like_1'),\
                                                        InlineKeyboardButton(text='Дизлайк', callback_data='like -1'))