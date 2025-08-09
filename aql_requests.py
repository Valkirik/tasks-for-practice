import sqlite3
conn = sqlite3.connect(":memory:") #creating db local
cursor = conn.cursor() #creating an object that we can make sql requests whith

cursor.execute("CREATE TABLE products ("
               "id INTEGER,"
               "name TEXT,"
               "category TEXT,"
               "price INTEGER,"
               "stock INTEGER,"
               "rating REAL)")

products = [(1, "Laptop", "electronics", 1200, 5, 4.7),
            (2, "Iphone", "electronics", 700, 3, 5.7),
            (3, "Headphone", "electronics", 930, 2, 4.4),
            (4, "Watch", "electronics", 150, 1, 3.9),
            (5, "Gun", "toys",  300, 7, 3.0),
            (6, "Monopoly", "boardgame", 1000, 5, 6.0),
            (7, "Chest", "boardgame", 1200, 3, 4.7),
            (8, "Ping Pong", "game", 3000, 2, 4.0)]

print(products)

cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)", products)
conn.commit()

# cursor.execute("SELECT * FROM products")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# cursor.execute("SELECT * FROM products ORDER BY price DESC")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# cursor.execute("SELECT * FROM products WHERE category = 'electronics' AND price > 100 AND price < 1000")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# cursor.execute("SELECT * FROM products WHERE rating >= 4.5 AND stock > 2")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# cursor.execute("SELECT * FROM products WHERE name LIKE '%on%'")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

("по убыванию: ORDER BY smth DESC"
 "найти подстоку WHERE smth LIKR '%smeth%'")




"""(9, 'Ball', 'Toys', 400, 7, 4.0)"""
