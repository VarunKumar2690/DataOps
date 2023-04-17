


-- Create a table for storing customer information
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50),
  phone VARCHAR(15)
);
-- Create a table for storing customer information
CREATE TABLE customers_1 (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50),
  phone VARCHAR(15)
);

-- Insert data into the customers table
INSERT INTO customers (id, name, email, phone)
VALUES (1, 'John Smith', 'john@example.com', '123-456-7890'),
       (2, 'Jane Doe', 'jane@example.com', '987-654-3210'),
       (3, 'Alice Johnson', 'alice@example.com', '555-555-5555');

-- Create a table for storing order information
CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_id INT,
  product VARCHAR(50),
  quantity INT,
  price DECIMAL(10, 2),
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Insert data into the orders table
INSERT INTO orders (id, customer_id, product, quantity, price)
VALUES (1, 1, 'Product A', 2, 19.99),
       (2, 1, 'Product B', 1, 9.99),
       (3, 2, 'Product A', 5, 19.99),
       (4, 3, 'Product C', 3, 14.99);

-- Retrieve customer and order information by joining customers and orders tables
SELECT c.id AS customer_id,
       c.name AS customer_name,
       c.email AS customer_email,
       o.id AS order_id,
       o.product AS order_product,
       o.quantity AS order_quantity,
       o.price AS order_price
FROM customers c
JOIN orders o ON c.id = o.customer_id;
