import sqlite3

# Question 4
# Among customers who place more than one order (more than a single unique order_id), what
# is the average difference between their first order and subsequent orders?

print('\n\n############# Question 4 ############')
db_connection = sqlite3.connect("../glossier_db.db")
cursor = db_connection.cursor()

query = """
WITH CustomerOrders AS (
    SELECT 
        customer_id,
        order_id,
        completed_at,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY completed_at) AS order_rank
    FROM 
        ORDERS
),
FirstOrder AS (
    SELECT 
        customer_id,
        completed_at AS first_order_date
    FROM 
        CustomerOrders
    WHERE 
        order_rank = 1
),
SubsequentOrders AS (
    SELECT 
        c.customer_id,
        c.completed_at AS subsequent_order_date,
        f.first_order_date,
        JULIANDAY(c.completed_at) - JULIANDAY(f.first_order_date) AS days_difference
    FROM 
        CustomerOrders c
    JOIN 
        FirstOrder f ON c.customer_id = f.customer_id
    WHERE 
        c.order_rank > 1
)

SELECT 
    AVG(days_difference) AS average_days_difference
FROM 
    SubsequentOrders;
"""

cursor.execute(query)
average_days_difference = cursor.fetchone()[0]
print("Average days difference between first and subsequent orders for repeat customers:", average_days_difference)

assert round(average_days_difference, 2) == 0.5, f"Expected average_days_difference to be 0.5, but got {average_days_difference:.2f}"

cursor.close()
db_connection.close()

print("Assertion passed: Average days difference between first and subsequent orders is as expected.")
