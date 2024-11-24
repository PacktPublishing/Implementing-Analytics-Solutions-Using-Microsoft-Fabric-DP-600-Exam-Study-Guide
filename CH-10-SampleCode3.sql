-- Performing a Left Outer Join in SQL
-- SQL script to join 'customers' and 'sales' tables based on customer_id.

SELECT * 
FROM customers c 
LEFT JOIN sales s ON c.customer_id = s.customer_id;
