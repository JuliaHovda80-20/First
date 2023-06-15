import sqlite3

# Встановлюємо з'єднання з базою даних
conn = sqlite3.connect('C:\\Users\\Юлія\\Desktop\\база даних для длмашки.sqlite')

# Створюємо курсор
cursor = conn.cursor()

# Виконуємо запит на вибірку
query = "SELECT * FROM users WHERE age > 30"
cursor.execute(query)

# Отримуємо результати
results = cursor.fetchall()

# Виводимо результати
for row in results:
    print(row)

# Закриваємо з'єднання
conn.close()




