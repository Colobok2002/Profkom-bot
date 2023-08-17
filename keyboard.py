from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


home = InlineKeyboardButton('🏠 Домой', callback_data='home')
b1 = InlineKeyboardButton('Выплаты', callback_data='Vyplaty')
b2 = InlineKeyboardButton('Общежития', callback_data='Obshchezhitiya')
b3 = InlineKeyboardButton('Профком', callback_data='Profkom')
b4 = InlineKeyboardButton('Узнать номер профсоюзного билета', callback_data='tikets')
b5 = InlineKeyboardButton('Санаторий-профилакторий', callback_data='sanat')
b6 = InlineKeyboardButton('Обратиться к модератору', callback_data='moder')

b7 = InlineKeyboardButton('Материальна помощь от университета', callback_data='my')
b8 = InlineKeyboardButton('Материальная помощь от профкома', callback_data='mp')


kb_home = InlineKeyboardMarkup(row_width=2)
kb_home.add(b1,b2,b3,b4,b5,b6)

VyplatyKb = InlineKeyboardMarkup(row_width=2)
VyplatyKb.add(b7,b8,home)