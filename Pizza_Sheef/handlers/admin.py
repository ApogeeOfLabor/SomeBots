from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from db.config_db import insert_value
from keyboards.client_kb import admin_keyboard
from src.headers import bot

ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# Получаем ID текущего модератора
async def check_id_moderator(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что надо хозяин???', reply_markup=admin_keyboard)
    await message.delete()


# Начало диалога загрузки нового пункта меню
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')
    else:
        await message.reply('Полож трубку!!!')


# Ловим первый ответ и пишем в словарь
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Теперь введи название')


# Ловим имя и пишем в словарь
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи описание')


#Ловим описание и пишем в словарь
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь укажи цену')


#Ловим цену и пишем в словарь
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)

        await insert_value(state)
        await state.finish()


# Выход из состояния
async def close_states(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        if await state.get_state():
            await state.finish()
            await message.reply('OK')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, Text(equals='Загрузить', ignore_case=True), state=None)
    dp.register_message_handler(close_states, commands='отмена', state="*")
    dp.register_message_handler(close_states, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(check_id_moderator, commands=['moderator'], is_chat_admin=True)
