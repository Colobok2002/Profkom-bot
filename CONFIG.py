from conf import * # Это для моего пользованяи можете удалить
import os

TOKEN = TOKEN # Токен бота

WEBHOOK_HOST = WEBHOOK_HOST #Хостинг для вебхуков

WEBHOOK_PATH = f'/webhook/{TOKEN}'

WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'

WEBAPP_PORT = 5000

pat_home = os.getcwd()

