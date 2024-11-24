-- Selecting Specific Customer Details
SELECT customer_id, customer_name
FROM customers
WHERE region = 'North America';

-- Aggregating Customer Count by Region
SELECT Region, COUNT(CustomerID) AS CustomerCount
FROM Customers
GROUP BY Region
ORDER BY CustomerCount DESC;


-- Joining Tables to Combine Customer and Sales Data
SELECT c.customer_name, s.sales_amount
FROM customers c
JOIN sales s ON c.customer_id = s.customer_id
WHERE s.sales_date > '2023-01-01';

-- Subquery to Retrieve Customers with Recent Purchases
SELECT customer_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM sales
    WHERE sales_date > '2023-01-01'
);


-- Using a Common Table Expression (CTE) for Aggregated Sales
WITH recent_sales AS (
    SELECT customer_id, SUM(sales_amount) AS total_sales
    FROM sales
    WHERE sales_date > '2023-01-01'
    GROUP BY customer_id
)
SELECT * FROM recent_sales;

-- Recursive Query with CTE for Hierarchical Data
WITH RecursiveCTE AS (
    SELECT employee_id, manager_id, employee_name
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.manager_id, e.employee_name
    FROM employees e
    JOIN RecursiveCTE r ON e.manager_id = r.employee_id
)
SELECT * FROM RecursiveCTE;


-- Creating an Index to Improve Query Performance
CREATE INDEX idx_customer_id ON customers(customer_id);

-- Partitioning a Table by Date for Performance Optimization
CREATE TABLE orders (
    order_id INT,
    order_date DATE
)
PARTITION BY RANGE(order_date) (
    PARTITION p1 VALUES LESS THAN ('2023-01-01'),
    PARTITION p2 VALUES LESS THAN ('2024-01-01')
);

-- Hash Partitioning Table by Customer ID
CREATE TABLE orders (
    order_id INT,
    order_date DATE,
    customer_id INT
)
WITH (DISTRIBUTION = HASH(customer_id), PARTITION BY RANGE(order_date));


-- Using EXPLAIN to Generate an Execution Plan
EXPLAIN SELECT customer_id, order_total
FROM orders
WHERE order_date > '2023-01-01';

-- Enabling Result Set Caching in Synapse
SET RESULT_SET_CACHING ON;



-- Window Function to Rank Employees by Salary
SELECT employee_id, salary,
       RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;

-- Calculating Cumulative Sales with SUM() OVER
SELECT order_id, order_date, sales_amount,
       SUM(sales_amount) OVER (ORDER BY order_date) AS cumulative_sales
FROM sales;


-- Query for Parallel Processing in SQL Pools
SELECT product_id, SUM(sales_amount)
FROM sales
GROUP BY product_id
ORDER BY SUM(sales_amount) DESC;
