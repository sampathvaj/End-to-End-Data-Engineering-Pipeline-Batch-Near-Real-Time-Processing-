-- Step 8.1: Create database
CREATE DATABASE sales_db;

-- Step 8.2: Use database
USE sales_db;

-- Step 8.3: Create clean sales table
CREATE TABLE sales_clean (
    order_id INT,
    order_date DATE,
    region VARCHAR(50),
    sales_amount FLOAT,
    profit FLOAT,
    year INT,
    month INT
);
