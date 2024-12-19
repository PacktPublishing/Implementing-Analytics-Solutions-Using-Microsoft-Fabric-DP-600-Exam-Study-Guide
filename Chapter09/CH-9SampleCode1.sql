-- SQL Script for Data Partitioning in Microsoft Fabric
-- Creates a partitioned SalesData table, splitting data into partitions based on SaleDate.

CREATE TABLE SalesData (
    SaleID int,
    SaleDate datetime,
    TotalAmount decimal
)
PARTITION BY RANGE (SaleDate) (
    PARTITION p1 VALUES LESS THAN ('2022-01-01'),
    PARTITION p2 VALUES LESS THAN ('2023-01-01'),
    PARTITION p3 VALUES LESS THAN ('2024-01-01')
);

-- Query to retrieve sales data within a specific date range for efficient scanning of relevant partitions.
SELECT SaleID, TotalAmount
FROM SalesData
WHERE SaleDate BETWEEN '2022-05-01' AND '2022-12-31';



-- Creating an Index on CustomerID for Optimization
-- Optimizes data retrieval by indexing the CustomerID column in the SalesData table.

CREATE INDEX idx_CustomerID
ON SalesData(CustomerID);

-- Optimized query using the index for faster retrieval.
SELECT CustomerID, TotalAmount
FROM SalesData
WHERE CustomerID = 12345;

-- Creating a Columnstore Index for Optimized Storage and Retrieval
-- Creates a clustered columnstore index on SalesData for optimized storage and retrieval of large datasets.

CREATE CLUSTERED COLUMNSTORE INDEX IDX_SalesData ON SalesData;


-- Viewing and Analyzing a Query Execution Plan in Microsoft Fabric
-- Enables STATISTICS PROFILE to analyze the query execution plan, useful for performance tuning.

SET STATISTICS PROFILE ON;
SELECT * FROM SalesData WHERE SaleDate > '2022-01-01';
SET STATISTICS PROFILE OFF;
