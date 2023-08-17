from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


home = InlineKeyboardButton('🏠 Домой', callback_data='home')

# .
b1 = InlineKeyboardButton('Выплаты', callback_data='b1')
# ..
b1_1 = InlineKeyboardButton('Материальна помощь от университета', callback_data='b1_1')
b1_2 = InlineKeyboardButton('Материальная помощь от профкома', callback_data='b1_2')

# .
b2 = InlineKeyboardButton('Степендии', callback_data='b2')

# ..
b2_1 = InlineKeyboardButton('ГАС', callback_data='b2_1')
b2_2 = InlineKeyboardButton('ПГСС', callback_data='b2_2')
b2_3 = InlineKeyboardButton('ГСС', callback_data='b2_3')
b2_4 = InlineKeyboardButton('ПГАС', callback_data='b2_4')

# ...
b2_4_1 = InlineKeyboardButton('Учебная', callback_data='b2_4_1')
b2_4_2 = InlineKeyboardButton('Научная', callback_data='b2_4_2')
b2_4_3 = InlineKeyboardButton('Культурно-творческая', callback_data='b2_4_3')
b2_4_4 = InlineKeyboardButton('Общественная', callback_data='b2_4_4')
b2_4_5 = InlineKeyboardButton('Спортивная', callback_data='b2_4_5')

# ..
b2_5 = InlineKeyboardButton('Стипендии от главы ЧР/ Стипендия администрации Чебоксар', callback_data='b2_5')

# ..
b2_6  = InlineKeyboardButton('Стипендии правительства и Президента РФ', callback_data='b2_6')

# ...
b2_6_1= InlineKeyboardButton('Стипендия Президента РФ', callback_data='b2_6_1')
b2_6_2 = InlineKeyboardButton('Стипендия правительства РФ', callback_data='b2_6_2')

# ..
b2_7 = InlineKeyboardButton('Дополнительные стипендии', callback_data='b2_7')

# ...
b2_7_1 = InlineKeyboardButton('Дополнительная стипендия для победителей и призеров олимпиад', callback_data='b2_7_1')
b2_7_2 = InlineKeyboardButton('Дополнительная стипендия для высокобальников', callback_data='b2_7_2')


# .
b3 = InlineKeyboardButton('Общежития', callback_data='b3')

# .
b4 = InlineKeyboardButton('Профком', callback_data='b4')

# .
b5 = InlineKeyboardButton('Узнать номер профсоюзного билета', callback_data='b5')

# .
b6 = InlineKeyboardButton('Санаторий-профилакторий', callback_data='b6')

# .
b7 = InlineKeyboardButton('Обратиться к модератору', callback_data='b7')





kb_home = InlineKeyboardMarkup(row_width=2)
kb_home.add(b1,b2,b3,b4,b5,b6)

VyplatyKb = InlineKeyboardMarkup(row_width=2)
VyplatyKb.add(b1_1,b1_2,home)