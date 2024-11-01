import sqlite3

# Question 1
# What is the total number of orders placed and average quantity per order? (Hint: just need to use
# the orders table)

print('\n\n############# Questsion 1 ############')
db_connection = sqlite3.connect("../glossier_db.db")
cursor = db_connection.cursor()
query = """
SELECT 
    COUNT(DISTINCT order_id) AS total_orders,
    AVG(order_quantity) AS average_quantity_per_order
FROM (
    SELECT order_id, SUM(quantity) AS order_quantity
    FROM ORDERS
    GROUP BY order_id
) AS order_totals;
"""

cursor.execute(query)
orders_data = cursor.fetchone()

total_orders, average_quantity_per_order = orders_data

print("Total orders:", total_orders)
print("Average quantity per order:", average_quantity_per_order)

assert total_orders == 3, f"Expected total_orders to be 3, but got {total_orders}"
assert round(average_quantity_per_order, 2) == 2.33, f"Expected average_quantity_per_order to be 2.33, but got {average_quantity_per_order:.2f}"

cursor.close()
db_connection.close()

print("Assertions passed: Total orders and average quantity per order are as expected.")
