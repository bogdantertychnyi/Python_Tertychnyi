import sqlite3 as sq
from data import data

with sq.connect('barbershop.db') as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS services")
    cur.execute("""CREATE TABLE IF NOT EXISTS services(
        master TEXT NOT NULL,
        client TEXT NOT NULL,
        gender TEXT NOT NULL,
        haircut TEXT NOT NULL,
        price INTEGER NOT NULL
    )""")

    cur.executemany("INSERT INTO services VALUES (?, ?, ?, ?, ?)", data)

    print("\nУслуги мастера Ивановой:")
    cur.execute("SELECT * FROM services WHERE master = 'Иванова А.В.'")
    for row in cur.fetchall():
        print(row)

    print("\nЖенские стрижки:")
    cur.execute("SELECT * FROM services WHERE gender = 'Ж'")
    for row in cur.fetchall():
        print(row)

    print("\nСтрижки дороже 1000:")
    cur.execute("SELECT * FROM services WHERE price > 1000")
    for row in cur.fetchall():
        print(row)

    cur.execute("DELETE FROM services WHERE haircut = 'Стрижка машинкой'")
    print("\nУдалена услуга 'Стрижка машинкой'")

    cur.execute("DELETE FROM services WHERE master = 'Козлов А.В.'")
    print("Удалены услуги мастера Козлова")

    cur.execute("DELETE FROM services WHERE client LIKE 'Фролов%'")
    print("Удалены услуги клиента Фролов")

    cur.execute("UPDATE services SET price = price + 200 WHERE haircut = 'Мужская стрижка'")
    print("\nЦена 'Мужской стрижки' увеличена на 200")

    cur.execute("UPDATE services SET master = 'Семенова Л.К.' WHERE master = 'Сидорова Л.М.'")
    print("Сидорова заменена на Семенову")

    cur.execute("UPDATE services SET haircut = 'Женская укладка' WHERE haircut = 'Женская стрижка'")
    print("Женская стрижка заменена на укладку")

    print("\nТаблица после всех изменений:")
    for row in cur.execute("SELECT * FROM services"):
        print(row)
