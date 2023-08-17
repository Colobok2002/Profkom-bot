from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btn_1 = InlineKeyboardButton('Личный кабинет', callback_data='button1')


kb_home = InlineKeyboardMarkup(row_width=2)
kb_home.add(btn_1)

