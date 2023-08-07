import json
import string
from aiogram import types, Dispatcher


async def echo_send(message: types.Message):
    if {word.lower().translate(str.maketrans('', '', string.punctuation + '№')) for word in message.text.split(' ')}.intersection(set(json.load(open('/home/vksource/Code/Python/Bots/Pizza_Sheef/src/cenz.json')))):
        await message.reply('Маты запрещены')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
