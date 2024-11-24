-- Creating a Partitioned Table for Sales Data
CREATE TABLE Sales (
    SaleID INT,
    SaleDate DATE,
    Amount DECIMAL(10, 2)
)
PARTITION BY RANGE (SaleDate);



-- SQL Query for Selecting Sales Data within a Date Range
DECLARE @StartDate DATE = '2023-01-01';
DECLARE @EndDate DATE = '2023-01-31';

SELECT SaleID, Amount
FROM Sales
WHERE SaleDate BETWEEN @StartDate AND @EndDate;


-- Indexing for Faster Data Retrieval
CREATE INDEX idx_SaleDate ON Sales(SaleDate);


-- Materialized Views for Efficient Data Access
CREATE MATERIALIZED VIEW MonthlySales AS
SELECT EXTRACT(MONTH FROM SaleDate) AS Month, SUM(Amount) AS TotalSales
FROM Sales
GROUP BY EXTRACT(MONTH FROM SaleDate);


-- ETL with SQL for Optimized Data Flow
SELECT customer_id, sales_amount
INTO raw_sales_data
FROM sales_data
WHERE sales_date >= '2023-01-01';
