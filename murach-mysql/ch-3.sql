/*
MySQL Examples - SELECT Statements
Chapter 3
*/

-- select database 'ap'
USE ap;

SELECT invoice_number, invoice_date, invoice_total
FROM invoices
ORDER BY invoice_total DESC
LIMIT 10;

SELECT invoice_id, invoice_number, invoice_date, invoice_total
FROM invoices
WHERE invoice_id = 10;

SELECT invoice_number, invoice_date, invoice_total
FROM invoices
WHERE invoice_date BETWEEN '2014-07-01' AND '2014-07-31'
ORDER BY invoice_date DESC;

SELECT invoice_number, invoice_date, invoice_total
FROM invoices
WHERE invoice_total > 20000
ORDER BY invoice_total DESC;

-- change to database 'om'
USE om;

SELECT 
    CONCAT(customer_last_name, ', ', customer_first_name) AS customer_name
FROM customers
ORDER BY customer_last_name
LIMIT 10;

SELECT 
    CONCAT(customer_last_name, ', ', customer_first_name) AS 'Customer Name',
    CONCAT(customer_city, ', ', customer_state, '  ', customer_zip) AS 'Customer Address'
FROM customers
ORDER BY customer_last_name
LIMIT 10;