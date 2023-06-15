import sqlite3

# Поточний шлях до бази даних SQLite
db_path = 'C:\\Users\\Юлія\\Desktop\\база даних для длмашки.sqlite'

# Встановлення з'єднання з базою даних
connection = sqlite3.connect(db_path)

# Створення курсора
cursor = connection.cursor()

# Виконання запиту
query = "SELECT COUNT(*) FROM users WHERE age > 30;"
cursor.execute(query)

# Отримання результатів
result = cursor.fetchone()[0]
print("Total count:", result)

# Закриття курсора і з'єднання з базою даних
cursor.close()
connection.close()