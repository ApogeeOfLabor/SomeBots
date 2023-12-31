from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from db.config_db import get_menu
from src.headers import bot
from keyboards.client_kb import client_keyboard


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "На связи!", reply_markup=client_keyboard)
        await message.delete()
    except Exception:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/KoenigPizzaSheefBot')


async def command_help(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Какое-то описание бота")
        await message.delete()
    except Exception:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/KoenigPizzaSheefBot')


async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, "ПН - ПТ с 09:00 до 21:00\nСБ - ВС с 09:00 до 23:00")


async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, "деревня Большое Пиценёво ул.Тестова 17")


async def pizza_menu(message: types.Message):
    for ret in await get_menu():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[3]}')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(pizza_open_command, Text(equals='Режим работы', ignore_case=True))
    dp.register_message_handler(pizza_place_command, Text(equals='Расположение', ignore_case=True))
    dp.register_message_handler(pizza_menu, Text(equals='Меню', ignore_case=True))
