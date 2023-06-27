query = "SELECT users.id, COUNT(purchases.id) AS purchases_count " \
        "FROM users " \
        "LEFT JOIN purchases ON users.id = purchases.user_id " \
        "GROUP BY users.id"

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    user_id = row[0]
    purchases_count = row[1]
    print(f"User ID: {user_id}, Purchases Count: {purchases_count}")
