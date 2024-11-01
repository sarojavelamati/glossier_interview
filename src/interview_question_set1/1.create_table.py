import sqlite3


db_connection = sqlite3.connect("../glossier_db.db")
print("\n\n******* DDL **********")
cursor = db_connection.cursor()
create_orders_table = """
CREATE TABLE IF NOT EXISTS ORDERS (
    customer_id INTEGER,
    order_id INTEGER,
    variant_id TEXT,
    quantity INTEGER,
    revenue REAL,
    completed_at TEXT,
    PRIMARY KEY (customer_id, order_id, variant_id));"""
create_products_table = """
CREATE TABLE IF NOT EXISTS PRODUCTS (
    product_id TEXT,
    product_name TEXT,
    variant_id TEXT,
    variant_shade TEXT,
    price REAL,
    PRIMARY KEY (product_id, variant_id));"""
create_users_table = """
CREATE TABLE IF NOT EXISTS USERS (
    customer_id INTEGER,
    customer_email TEXT,
    first_name TEXT,
    last_name TEXT,
    country TEXT,
    created_at TEXT,
    PRIMARY KEY (customer_id, customer_email));"""
cursor.execute(create_products_table)
cursor.execute(create_users_table)
cursor.execute(create_orders_table)
db_connection.commit()
cursor.close()
db_connection.close()
print("Tables created successfully.\n\n")
