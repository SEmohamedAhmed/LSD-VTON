-- Create new database
-- Drop database EcommerceDB;
CREATE DATABASE EcommerceDB;
go
-- Use the newly created database
USE EcommerceDB;
go
-- Create Product table
CREATE TABLE Product (
    product_id VARCHAR(32) NOT NULL UNIQUE,
    name VARCHAR(64) NOT NULL,
);
-- Drop the Product table
--DROP TABLE Product;
GO
-- Create Customer table with auto-increment customer_id
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY IDENTITY(1,1) ,
    username VARCHAR(64) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
);

go

CREATE TABLE Cart (
	customer_id INT FOREIGN KEY REFERENCES Customer(customer_id),
	product_id VARCHAR(32) FOREIGN KEY REFERENCES Product(product_id)
);
