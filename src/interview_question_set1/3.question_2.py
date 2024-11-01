import sqlite3

# Question 2
# For each order ID, what is the total number of unique products purchased and number of unique
# variants purchased?

print('\n\n############# Question 2 ############')
db_connection = sqlite3.connect("../glossier_db.db")
cursor = db_connection.cursor()
query = """
SELECT 
    order_id,
    COUNT(DISTINCT product_id) AS unique_products,
    COUNT(DISTINCT ORDERS.variant_id) AS unique_variants
FROM 
    ORDERS
JOIN 
    PRODUCTS ON ORDERS.variant_id = PRODUCTS.variant_id
GROUP BY 
    order_id;
"""
cursor.execute(query)
results = cursor.fetchall()
print("Unique products and variants per order ID:")
for row in results:
    order_id, unique_products, unique_variants = row
    print(f"Order ID: {order_id}, Unique Products: {unique_products}, Unique Variants: {unique_variants}")

# Expected unique products and variants for order 123
# Expected unique products and variants for order 234
# Expected unique products and variants for order 456
assert results == [
    (123, 1, 2),
    (234, 1, 1),
    (456, 1, 1)
], f"Unexpected result: {results}"

cursor.close()
db_connection.close()

print("Assertions passed: Unique products and variants per order ID are as expected.")
