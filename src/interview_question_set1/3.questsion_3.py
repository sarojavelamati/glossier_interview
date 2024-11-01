import sqlite3

# Questson 3
# For each country, what is the average order value of first time customers?

print('\n\n############# Question 3 ############')
db_connection = sqlite3.connect("../glossier_db.db")
cursor = db_connection.cursor()
query = """
SELECT 
    country,
    AVG(revenue) AS average_order_value
FROM 
    ORDERS
JOIN 
    USERS ON ORDERS.customer_id = USERS.customer_id
WHERE 
    (ORDERS.customer_id, ORDERS.completed_at) IN (
        SELECT customer_id, MIN(completed_at)
        FROM ORDERS
        GROUP BY customer_id
    )
GROUP BY 
    country;
"""

cursor.execute(query)
results = cursor.fetchall()
print("Average order value of first-time customers per country:")
for row in results:
    country, average_order_value = row
    print(f"Country: {country}, Average Order Value: {average_order_value}")

assert results == [
    ('Canada', 28.0),
    ('United States', 22.0)
], f"Unexpected result: {results}"

cursor.close()
db_connection.close()
print("Assertions passed: Average order value of first-time customers per country is as expected.")

