/*
MySQL Examples - SELECT Statements
Chapter 3
*/

-- select database 'ap'
USE ap;

/* simple query with ORDER BY, DESC and LIMIT */
SELECT invoice_number, invoice_date, invoice_total
FROM invoices
ORDER BY invoice_total DESC
LIMIT 10;

/* add WHERE */
SELECT invoice_id, invoice_number, invoice_date, invoice_total
FROM invoices
WHERE invoice_id = 10;

/* BETWEEN and AND */
SELECT invoice_number, invoice_date, invoice_total
FROM invoices
WHERE invoice_date BETWEEN '2014-07-01' AND '2014-07-31'
ORDER BY invoice_date DESC;

/* > operator */
SELECT invoice_number, invoice_date, invoice_total
FROM invoices
WHERE invoice_total > 20000
ORDER BY invoice_total DESC;

-- change to database 'om'
USE om;

/* CONCAT */
SELECT 
    CONCAT(customer_last_name, ', ', customer_first_name) AS customer_name
FROM customers
ORDER BY customer_last_name
LIMIT 10;

/* CONCAT */ 
SELECT 
    CONCAT(customer_last_name, ', ', customer_first_name) AS 'Customer Name',
    CONCAT(customer_city, ', ', customer_state, '  ', customer_zip) AS 'Customer Address'
FROM customers
ORDER BY customer_last_name
LIMIT 10;

/* CONCAT and LEFT */
SELECT
    customer_first_name,
    customer_last_name,
    CONCAT(LEFT(customer_first_name, 1), LEFT(customer_last_name, 1)) AS initials
FROM customers
ORDER BY customer_last_name
LIMIT 10;

/* DATE_FORMAT */
SELECT order_date,
    DATE_FORMAT(order_date, '%m/%d/%y') AS 'MM/DD/YY',
    DATE_FORMAT(order_date, '%e-%b-%Y') AS 'DD-Mon-YYYY'
FROM orders
LIMIT 10;