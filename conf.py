BOTTUPE = 'test'

text_add_key = """В первую очередь в бот должен быть добавлен ключь API , для его получения пройдитесь по шагам\n\n
1) Зайдите в личный кабинет Wildberries → Настройки → Доступ к API (ссылка) (https://seller.wildberries.ru/supplier-settings/access-to-new-api).\n\n
2) После чего вам необходимо сгенерировать новый ключь дать ему название и обязательно выбрать пункт статистика
(<b>Обратите внимание, что ключ отображается ТОЛЬКО в момент создания. Его надо сохранить, потому что больше его отобразить будет нельзя</b>)\n\n
3) Скопируйте токен и отправьте в сообщении боту."""


TOKEN = '6650917885:AAH0z4ybmWo8Y7-KIcKjqerf76S7r33TT9I'
WEBHOOK_HOST = f'https://66d7-89-151-178-35.ngrok-free.app'
name_bot = '@CHGY_Profkom_bot'

WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

print(WEBHOOK_URL)

WEBAPP_HOST = '0.0.0.0'

WEBAPP_PORT = 5000
