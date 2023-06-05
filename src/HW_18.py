import sqlite3

# Встановлення з'єднання з базою даних
conn = sqlite3.connect('database.db')

# Створення курсора для виконання SQL-запитів
cursor = conn.cursor()

# # Виконання SQL-запиту для створення таблиці
# quary = ("CREATE TABLE IF NOT EXIST users ("
#          "id INTEGER PRIMARY KEY AUTOINCREMENT ,"
#          "first_name TEXT, not null
#         unique,"
#          "last_name TEXT,not null
#         unique"
#          "age INTEGER)")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT not null
        unique,
        last_name TEXT not null
        unique,
        age INTEGER not null
    )
''')
#
# conn.commit()
#
#
# data = [('Juliia','Hovda', 28),
#         ('Juli','Hovd', 27),
#         ('Jul','Hov', 26),
#         ('Juliiaaaa','Hovdaaaaa', 29),
#         ('Ju','Hovddddda', 20)
#         ]
#
#
# quary = "INSERT INTO users (first_name,last_name,age) VALUES (?,?,?)"
#
# cursor.executemany(quary, data)
#  Збереження змін до бази даних
# conn.commit()
