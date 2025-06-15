import sqlite3 as sq

with sq.connect('zak-tovar') as con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS zakazi')
    cur.execute("""CREATE TABLE IF NOT EXISTS zakazi(
    itm_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    company TEXT NOT NULL,
    zak_date DATE NOT NULL,
    srok INTEGER NOT NULL CHECK(srok >= 1 AND srok <= 10),
    price INTEDER NOT NULL
                )""")