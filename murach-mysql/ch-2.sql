/*
 * ----------------------------------------------
 * MySQL Examples - MySQL Workbench and MySQL 
 *                  Command Line Client
 * ----------------------------------------------
 */

SELECT vendor_name 
FROM vendors;

SELECT COUNT(*) AS number_of_invoices,
    SUM(invoice_total) AS grand_invoice_total
FROM invoices;

SELECT vendor_name, vendor_city, vendor_state
FROM vendors
ORDER BY vendor_name;

SELECT COUNT(*) AS number_of_invoices,
    SUM(invoice_total - payment_total - credit_total) AS total_due
FROM invoices
WHERE invoice_total - payment_total - credit_total > 0;

SELECT vendor_name, vendor_city
FROM vendors
WHERE vendor_id = 34;

SELECT COUNT(*) AS number_of_invoices,
    SUM(invoice_total - payment_total - credit_total) AS total_due
FROM invoices
WHERE vendor_id = 34;

/*
-- Using the MySQL Command Line Client

mysql> show databases;

mysql> use ap;

mysql> select invoice_number from invoices limit 10;

mysql> describe ap;
*/