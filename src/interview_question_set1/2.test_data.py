import sqlite3

# INSERT OR IGNORE  -> will eliminate dulicate values.

db_connection = sqlite3.connect("../glossier_db.db")
cursor = db_connection.cursor()
orders_data = [
    (1, 123, 'd1', 2, 30.0, '2023-10-01'),
    (1, 123, 'd4', 1, 14.0, '2023-10-01'),
    (1, 234, 'd4', 2, 28.0, '2023-10-02'),
    (2, 456, 'd2', 2, 28.0, '2023-10-02')
]
products_data = [
    ('a', 'A Cleanser', 'a1', None, 22.0),
    ('d', 'D Paint', 'd1', 'Pink', 18.0),
    ('d', 'D Paint', 'd2', 'Purple', 18.0),
    ('d', 'D Paint', 'd3', 'Red', 18.0),
    ('d', 'D Paint', 'd4', 'Maroon', 18.0)
]

users_data = [
    (1, 'one@glossier.com', 'One', 'Glossier', 'United States', '2023-01-01'),
    (1, 'one+one@glossier.com', 'One', 'Glossier', 'United States', '2023-01-02'),
    (2, 'two@glossier.com', 'Two', 'Glossier', 'Canada', '2023-02-01')
]

cursor.executemany("""
INSERT OR IGNORE INTO ORDERS (customer_id, order_id, variant_id, quantity, revenue, completed_at)
VALUES (?, ?, ?, ?, ?, ?);
""", orders_data)

cursor.executemany("""
INSERT OR IGNORE INTO PRODUCTS (product_id, product_name, variant_id, variant_shade, price)
VALUES (?, ?, ?, ?, ?);
""", products_data)

cursor.executemany("""
INSERT OR IGNORE INTO USERS (customer_id, customer_email, first_name, last_name, country, created_at)
VALUES (?, ?, ?, ?, ?, ?);
""", users_data)

db_connection.commit()
cursor.close()
db_connection.close()

print("Test data inserted successfully.\n\n")
