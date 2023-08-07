from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_env, find_env

load_env(find_env('.env'))

storage = MemoryStorage()

bot = Bot(os.getenv('token'))
dp = Dispatcher(bot, storage=storage)
