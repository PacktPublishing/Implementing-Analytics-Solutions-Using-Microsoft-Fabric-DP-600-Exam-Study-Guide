-- T-SQL Code for Creating a Table
-- This script creates an 'Employee' table within the specified database and schema.
CREATE TABLE [jaswarehouse].[dbo].[Employee]
(
    EmployeeID INT NOT NULL,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    DateOfBirth DATE,
    Position VARCHAR(255)
);
GO


-- T-SQL Code for Inserting Data into the Table
-- This script inserts sample employee records into the 'Employee' table.
INSERT INTO [jaswarehouse].[dbo].[Employee]  
    (EmployeeID, FirstName, LastName, DateOfBirth, Position) 
VALUES 
    (1, 'John', 'Doe', '1985-07-10', 'Manager'),
    (2, 'Jane', 'Smith', '1990-02-15', 'Developer'),
    (3, 'Alice', 'Johnson', '1988-03-22', 'Designer'),
    (4, 'Bob', 'Brown', '1975-11-05', 'Analyst'),
    (5, 'Charlie', 'Davis', '1992-06-30', 'Tester');



-- Example Stored Procedure to Update Employee Salary
-- This stored procedure allows updating an employee's salary based on EmployeeID.
CREATE PROCEDURE UpdateEmployeeSalary
    @EmployeeID INT,
    @NewSalary DECIMAL(10, 2)
AS
BEGIN
    UPDATE Employees
    SET Salary = @NewSalary
    WHERE EmployeeID = @EmployeeID;

    IF @@ROWCOUNT = 0
    BEGIN
        RAISERROR('Employee not found', 16, 1);
    END
END;



-- SQL for Partitioning and Creating an Index
-- Creates a 'Sales' table partitioned by SaleDate and adds an index on SaleDate for optimized queries.
CREATE TABLE Sales (
    SaleID INT,
    SaleDate DATE,
    Amount DECIMAL(10, 2)
)
PARTITION BY RANGE (SaleDate);

CREATE INDEX idx_SaleDate ON Sales(SaleDate);



-- SQL Query to Retrieve Data for a Specific Date Range
-- Retrieves Sales data within a specific date range.
SELECT SaleID, Amount
FROM Sales
WHERE SaleDate BETWEEN '2023-01-01' AND '2023-01-31';


-- Creating a Materialized View
-- This view calculates total sales by month, precomputing results for fast access.
CREATE MATERIALIZED VIEW mv_MonthlySales AS
SELECT EXTRACT(MONTH FROM SaleDate) AS Month, SUM(Amount) AS TotalSales
FROM Sales
GROUP BY EXTRACT(MONTH FROM SaleDate);



-- Updating Statistics for Query Optimization
-- Updates statistics on the 'Sales' table to improve query performance.
UPDATE STATISTICS Sales;


-- Granting Select Permissions to a Role
-- Grants 'SELECT' permissions on the 'Sales' table to a role called 'SalesAnalystRole'.
GRANT SELECT ON Sales TO SalesAnalystRole;
