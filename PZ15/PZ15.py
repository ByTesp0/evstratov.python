# Приложение ЗАКАЗЫ ТОВАРОВ для автоматизированного контроля заказот
# гортовой фирмы. Таблица Заказы должна содержать информацио о товарах со
# следующей структурой
# записи: Код товара, Наименование товара, Заказчик
# (наименование организации, возможны повторяющиеся значения), Дата заказа, Срок
# исполнения (от 1 до 10 дней), Стоимость заказа.

import sqlite3 as sq

with sq.connect('zak-tovar.db') as con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS zakazi')
    cur.execute("""CREATE TABLE IF NOT EXISTS zakazi(
    zak_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    company TEXT NOT NULL,
    zak_date DATE NOT NULL,
    srok INTEGER NOT NULL CHECK(srok >= 1 AND srok <= 10),
    price INTEDER NOT NULL
                )""")

    info = [
        (1, 'заказ 1', 'компания 1', '2025-1-13', 3, 1200),
        (2, 'заказ 2', 'компания 2', '2025-1-21', 2, 800),
        (3, 'заказ 3', 'компания 3', '2025-1-26', 8, 2000),
        (4, 'заказ 4', 'компания 4', '2025-2-4', 5, 1000),
        (5, 'заказ 5', 'компания 4', '2025-2-4', 7, 570),
        (6, 'заказ 6', 'компания 5', '2025-2-24', 9, 863),
        (7, 'заказ 7', 'компания 6', '2025-3-4', 3, 3200),
        (8, 'заказ 8', 'компания 7', '2025-3-10', 9, 2100),
        (9, 'заказ 9', 'компания 8', '2025-3-11', 6, 1200),
        (10, 'заказ 10', 'компания 9', '2025-3-17', 10, 2790)
    ]

    cur.executemany("INSERT INTO zakazi VALUES (?, ?, ?, ?, ?, ?)", info)

    cur.execute("SELECT * FROM zakazi WHERE company = 'компания 4'")
    print(f'все заказы компании 4: ', cur.fetchall())
    cur.execute("SELECT * FROM zakazi WHERE price <= 1000")
    print(f'все заказы стоимостью <= 1000: ', cur.fetchall())
    cur.execute("SELECT * FROM zakazi WHERE zak_id > 5")
    print(f'все заказы у которых zak_id > 5: ', cur.fetchall())

    cur.execute("UPDATE zakazi SET company = 'компания 1' WHERE price = 1200")
    cur.execute("UPDATE zakazi SET zak_date = '2025-1-25' WHERE price < 1000")
    cur.execute("UPDATE zakazi SET srok = 4 WHERE price >= 1500")

    cur.execute("DELETE FROM zakazi WHERE name = 'заказ 1'")
    cur.execute("DELETE FROM zakazi WHERE zak_id = 6")
    cur.execute("DELETE FROM zakazi WHERE price = 1000")