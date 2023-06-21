# запит, який виведе дату покупки і імʼя користувача, що її здійснив.

query = "SELECT purchases.id, purchases.date, users.first_name, users.last_name " \
        "FROM purchases " \
        "JOIN users ON purchases.user_id = users.id"

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    purchase_id = row[0]
    purchase_date = row[1]
    first_name = row[2]
    last_name = row[3]
    print(f"Purchase ID: {purchase_id}, Purchase Date: {purchase_date}, User: {first_name} {last_name}")
