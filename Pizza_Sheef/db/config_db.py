import sqlite3


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

