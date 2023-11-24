from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton, WebAppInfo, ReplyKeyboardMarkup

builder = ReplyKeyboardBuilder()
form_button = KeyboardButton(text='Перейти в форму', web_app=WebAppInfo(url='https://yandex.ru/'))
builder.add(form_button)
markup = ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)