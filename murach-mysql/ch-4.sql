/*
 * ----------------------------------------------
 * MySQL Examples - JOIN Statements
 * ----------------------------------------------
 */

USE ap;

/* inner join using aliases for tables */
SELECT i.invoice_number, v.vendor_name
FROM vendors v
INNER JOIN invoices i
    ON v.vendor_id = i.vendor_id
ORDER BY i.invoice_number LIMIT 10;

/* another join example */
SELECT 
    i.invoice_number, 
    v.vendor_name, 
    i.invoice_due_date,
    i.invoice_total - i.payment_total - i.credit_total AS balance_due
FROM vendors v
JOIN invoices i
    ON v.vendor_id = i.vendor_id
WHERE i.invoice_total - i.payment_total - i.credit_total > 0
ORDER BY i.invoice_due_date DESC;

/* with column headers */
SELECT 
    i.invoice_number AS "Invoice Number", 
    v.vendor_name AS "Vendor Name", 
    i.invoice_due_date AS "Invoice Due Date",
    i.invoice_total - i.payment_total - i.credit_total AS "Balance Due"
FROM vendors v
JOIN invoices i
    ON v.vendor_id = i.vendor_id
WHERE i.invoice_total - i.payment_total - i.credit_total > 0
ORDER BY i.invoice_due_date DESC;

/* join to table in another database */
SELECT 
    vendor_name, 
    customer_last_name, 
    customer_first_name, 
    vendor_state AS state, 
    vendor_city AS city
FROM vendors v
JOIN om.customers c
    ON v.vendor_zip_code = c.customer_zip
ORDER BY state, city, customer_last_name;

/* left outer join */
SELECT v.vendor_name, i.invoice_number, i.invoice_total
FROM vendors v
LEFT JOIN invoices i
    ON v.vendor_id = i.vendor_id
ORDER BY v.vendor_name;

/* union example */
SELECT 'Active' AS source, invoice_number, invoice_date, invoice_total
FROM active_invoices
    WHERE invoice_date >= '2014-06-01'
UNION
SELECT 'Paid' AS source, invoice_number, invoice_date, invoice_total
FROM paid_invoices
    WHERE invoice_date >= '2014-06-01'
ORDER BY invoice_total DESC;
