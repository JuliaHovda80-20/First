import random
from datetime import datetime
import sqlite3

# Конфігурація
CREATE_DATA = False

# Встановлення з'єднання з базою даних
conn = sqlite3.connect('bookshop.db')

# Створення курсора для виконання SQL-запитів
cursor = conn.cursor()


table_users = ("CREATE TABLE IF NOT EXISTS users("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "first_name TEXT,"
               "last_name TEXT,"
               "age INTEGER NOT NULL) ")


table_publishing_house = ("CREATE TABLE IF NOT EXISTS publishing_house ("
                          "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                          "name TEXT,"
                          "rating INTEGER DEFAULT 5)")

table_books = ("CREATE TABLE IF NOT EXISTS books("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "title TEXT,"
               "author TEXT,"
               "year INTEGER,"
               "price INTEGER NOT NULL,"
               "publishing_house_id INTEGER, "
               "FOREIGN KEY (publishing_house_id) REFERENCES publishing_house (id))")


table_purchases = ("CREATE TABLE IF NOT EXISTS purchases("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "user_id INTEGER NOT NULL,"
                   "book_id INETEGER NOT NULL,"
                   "date TEXT DEFAULT CURRENT_TIMESTAMP,"
                   "FOREIGN KEY (user_id) REFERENCES users (id),"
                   "FOREIGN KEY (book_id) REFERENCES books (id))")


cursor.execute(table_users)
cursor.execute(table_publishing_house)
cursor.execute(table_books)
cursor.execute(table_purchases)

# Наповнюємо таблицю users даними
# first_name,last_name,age

first_name = ["Ivan","Mykola","Julia","Ihor","Erika","Mandolina","Traktoruna","Dmytro","Oksana","Volodymyr"]
last_name = ["Kozak","Hovda","Mamchur","Ivaniv","Kovalchuk","Roy","Senko","Radmyr","Kiziak","Popina"]

# Створення рандомної таблиці з набором імен прізвищ та випадковим чином обраного віку
if CREATE_DATA:
    users = []
    for _ in range(60):
        users.append(
            (random.choice(first_name),random.choice(last_name),random.randint(20,80))
        )

    cursor.executemany("INSERT INTO users (first_name, last_name, age)"
                       "VALUES (?,?,?)",users)


# Наповнюємо таблицю publishing_house даними
# name ,rating

    name = ["vivat","staryi_lev","folio","gvara","svichado","ababagalamaga","capreze"]

    publishing_house = []
    for _ in range (8):
        publishing_house.append(
            (random.choice(name),random.randint(1,5))
        )

    cursor.executemany("INSERT INTO publishing_house (name,rating)"
                       "VALUES (?,?)",publishing_house)

    # Наповнюємо таблицю books даними
    # title, author, year , price, publishing_house_id
    title = ["Sara Says No!","The Umbrella","Winnie-The-Pooh and All, All, All","Dangerous Journey","Billy Budd",
             "The Coldest Place on Earth "," The Phantom of the Opera","The Wonderful Wizard of Oz"]
    author = ["Norman Whitney","Harris Clare","A. A. Milne","Alwyn Cox","Herman Melville","Tim Vicary","Gaston Leroux "," Frank Baum"]

    books = []
    for _ in range(8):
        books.append(
            (random.choice(title),random.choice(author),random.randint(1994,2023),random.randint(100,2005),random.randint(1,5))
        )

    cursor.executemany("INSERT INTO books (title, author, year , price, publishing_house_id)"
                       "VALUES (?,?,?,?,?)",books)

    # user_id, book_id ,date "

    purchases = []
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for _ in range(60):
        purchases.append(
            (random.randint(1,60),random.randint(1,8),date)
        )

    cursor.executemany("INSERT INTO purchases (user_id, book_id, date) VALUES (?, ?, ?)", purchases)

    # Збереження змін до бази даних та закриття з'єднання
    conn.commit()

query = "SELECT books.title, COUNT(purchases.id) AS sales_count " \
        "FROM books " \
        "LEFT JOIN purchases ON books.id = purchases.book_id " \
        "GROUP BY books.title " \
        "ORDER BY sales_count DESC"

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    title = row[0]
    sales_count = row[1]
    print(f"Title: {title}, Sales Count: {sales_count}")

