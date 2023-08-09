from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv('.env'))

storage = MemoryStorage()

bot = Bot(os.getenv('token'))
dp = Dispatcher(bot, storage=storage)
