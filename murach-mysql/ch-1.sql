/*
MySQL Examples - Getting Started
Chapter 1
*/

-- select database
USE ap;

-- run query on invoices table
SELECT 
    invoice_id, 
    invoice_number, 
    invoice_date, 
    invoice_total, 
    payment_total, 
    credit_total,
    invoice_total - payment_total - credit_total AS balance_due
FROM invoices
    WHERE invoice_total - payment_total - credit_total > 0
ORDER BY invoice_date