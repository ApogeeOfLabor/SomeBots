from handlers import client, other, admin
from aiogram.utils import executor
from db.config_db import make_db
from src.headers import dp


async def on_startup(_):
    make_db()
    print('Бот вышел в онлайн!')


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
