import sqlite3

# Поточний шлях до бази даних SQLite
db_path = 'C:\\Users\\Юлія\\Desktop\\база даних для длмашки.sqlite'

# Встановлення з'єднання з базою даних
connection = sqlite3.connect(db_path)

# Створення курсора
cursor = connection.cursor()

# Виконання запиту
query = "SELECT age, COUNT(*) as user_count FROM users GROUP BY age ORDER BY user_count DESC;"
cursor.execute(query)

# Отримання результатів
results = cursor.fetchall()
for row in results:
    age = row[0]
    user_count = row[1]
    print(f"Age: {age}, User Count: {user_count}")

# Закриття курсора і з'єднання з базою даних
cursor.close()
connection.close()
