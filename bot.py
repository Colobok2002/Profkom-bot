import logging
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from sql_beek import selekt ,add,update
from CONFIG import *
from keyboard import kb_home ,VyplatyKb , home




bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("menu", "Меню"),
    #     types.BotCommand("clear", "Очистка"),
    #     types.BotCommand("addcanl", "Добавить канал для уведомлений"),
    ])

@dp.message_handler(commands=['clear'])
async def cleaar(message: types.Message):
    user_id = message.from_user.id

    mes_id = message.message_id
    try:
        while True:
            await bot.delete_message(chat_id=user_id, message_id=mes_id)
            mes_id -= 1
    except:
        None


@dp.message_handler(commands=['start', 'menu'])
async def start(message: types.Message):

    await set_default_commands(dp)
  
    await bot.delete_message(message.from_user.id, message.message_id)

    await bot.send_message(message.from_id, text = "Hello yapta",reply_markup=kb_home)

        
@dp.callback_query_handler(lambda c: c.data == 'home')
async def process_callback_button1(callback_query: types.CallbackQuery):

    await bot.edit_message_text("Hello yapta", callback_query.from_user.id, callback_query.message.message_id,reply_markup=kb_home)


@dp.callback_query_handler(lambda c: c.data == 'Vyplaty')
async def process_callback_button1(callback_query: types.CallbackQuery):

    await bot.edit_message_text("Выплаты", callback_query.from_user.id, callback_query.message.message_id,reply_markup=VyplatyKb)


@dp.callback_query_handler(lambda c: c.data == 'my')
async def process_callback_button1(callback_query: types.CallbackQuery):

    await bot.edit_message_text("Материальна помощь от университета", callback_query.from_user.id, callback_query.message.message_id,reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('◀️ Назад', callback_data='Vyplaty'),home))

@dp.callback_query_handler(lambda c: c.data == 'mp')
async def process_callback_button1(callback_query: types.CallbackQuery):

    await bot.edit_message_text("Материальная помощь от профкома", callback_query.from_user.id, callback_query.message.message_id,reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('◀️ Назад', callback_data='Vyplaty'),home))



@dp.callback_query_handler(lambda c: c.data and c.data.startswith('edit_nev_mess'))
async def process_callback_edit_nev_mess(callback_query: types.CallbackQuery):

    key = callback_query.data.split('?')[1].split('=')

    if key[0] == 'nev_orders':
        update(callback_query.from_user.id,{'nev_order':key[1]})
    if key[0] == 'nev_orders_otk':
        update(callback_query.from_user.id,{'nev_order_otk':key[1]})
    if key[0] == 'nev_sales':
        update(callback_query.from_user.id,{'nev_sale':key[1]})
    if key[0] == 'nev_sales_otk':
        update(callback_query.from_user.id,{'nev_sale_otk':key[1]})\

    kb_yvid = InlineKeyboardMarkup(row_width=1)

    kesh = selekt(callback_query.from_user.id)

    nev_orders = kesh['nev_order']

    nev_orders_otk = kesh['nev_order_otk']

    nev_sales = kesh['nev_sale']

    nev_sales_otk = kesh['nev_sale_otk']

    if nev_orders == 1:
        kb_yvid.add(InlineKeyboardButton(f"🔔 Новые заказы", callback_data=f"edit_nev_mess?nev_orders=0"))
    else:
        kb_yvid.add(InlineKeyboardButton(f"🔕 Новые заказы", callback_data=f"edit_nev_mess?nev_orders=1"))

    if nev_orders_otk == 1:
        kb_yvid.add(InlineKeyboardButton(f"🔔 Новые отказы по заказам", callback_data=f"edit_nev_mess?nev_orders_otk=0"))
    else:
        kb_yvid.add(InlineKeyboardButton(f"🔕 Новые отказы по заказам", callback_data=f"edit_nev_mess?nev_orders_otk=1"))

    if nev_sales == 1:
        kb_yvid.add(InlineKeyboardButton(f"🔔 Новые продажи", callback_data=f"edit_nev_mess?nev_sales=0"))
    else:
        kb_yvid.add(InlineKeyboardButton(f"🔕 Новые продажи", callback_data=f"edit_nev_mess?nev_sales=1"))
    if nev_sales_otk == 1:
        kb_yvid.add(InlineKeyboardButton(f"🔔 Новые возвраты по продажам", callback_data=f"edit_nev_mess?nev_sales_otk=0"))
    else:
        kb_yvid.add(InlineKeyboardButton(f"🔕 Новые возвраты по продажам", callback_data=f"edit_nev_mess?nev_sales_otk=01"))

    kb_yvid.add(btn_5)

    await  bot.edit_message_text(chat_id=callback_query.from_user.id,
                                 message_id=selekt(callback_query.from_user.id)['last_msg_bot'],
                                 text=f'Включите/выкоючите необходимые уведомления\n\n',
                                 reply_markup=kb_yvid)

@dp.message_handler()
async def obrabotka(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,text="qwertt")

       
def start_bot():
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
if __name__ == '__main__':
    start_bot()