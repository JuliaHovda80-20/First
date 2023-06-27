query = "SELECT books.author, SUM(books.price) AS total_sales, COUNT(purchases.id) AS purchases_count " \
        "FROM books " \
        "JOIN purchases ON books.id = purchases.book_id " \
        "GROUP BY books.author"

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    author = row[0]
    total_sales = row[1]
    purchases_count = row[2]
    print(f"Author: {author}, Total Sales: {total_sales}, Purchases Count: {purchases_count}")
