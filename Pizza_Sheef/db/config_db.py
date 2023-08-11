import sqlite3
from aiogram import types
from src.headers import bot


def make_db():
    global base, cursor
    base = sqlite3.connect("db.sqlite")
    cursor = base.cursor()
    if base:
        print("DB connect OK!")
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def insert_value(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def clear_value(data):
    cursor.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()


async def get_menu():
    return cursor.execute('SELECT * FROM menu').fetchall()
