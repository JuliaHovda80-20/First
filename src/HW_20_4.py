query = "SELECT users.id, users.first_name, users.last_name, SUM(books.price) AS total_purchases " \
        "FROM users " \
        "JOIN purchases ON users.id = purchases.user_id " \
        "JOIN books ON purchases.book_id = books.id " \
        "GROUP BY users.id"

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    user_id = row[0]
    first_name = row[1]
    last_name = row[2]
    total_purchases = row[3]
    print(f"User ID: {user_id}, User: {first_name} {last_name}, Total Purchases: {total_purchases}")
