/*
 * ----------------------------------------------
 * MySQL Examples - Subqueries
 * ----------------------------------------------
 */

/* subquery with WHERE */
SELECT
    invoice_number,
    invoice_date,
    invoice_total
FROM invoices
    WHERE invoice_total >
        (SELECT AVG(invoice_total) FROM invoices)
ORDER BY invoice_total;

/* invoices and vendors joined with subquery */
SELECT
    v.vendor_name,
    i.invoice_number,
    i.invoice_date,
    i.invoice_total
FROM invoices i 
    JOIN vendors v ON i.vendor_id = v.vendor_id
WHERE v.vendor_id IN
    (SELECT vendor_id 
    FROM vendors 
    WHERE vendor_state = 'CA')
ORDER BY v.vendor_name, i.invoice_date;

/* vendors without invoices */
SELECT
    vendor_id,
    vendor_name,
    vendor_state
FROM vendors
WHERE vendor_id NOT IN
    (SELECT DISTINCT vendor_id FROM invoices)
ORDER BY vendor_id;

/* ALL */
SELECT
    v.vendor_name,
    i.invoice_number,
    i.invoice_total
FROM invoices i
    JOIN vendors v ON i.vendor_id = v.vendor_id
WHERE invoice_total > ALL
    (SELECT invoice_total
    FROM invoices
    WHERE vendor_id = 34)
ORDER BY v.vendor_name;

/* ANY */
SELECT
    v.vendor_name,
    i.invoice_number,
    i.invoice_total
FROM vendors v
    JOIN invoices i ON v.vendor_id = i.vendor_id
WHERE invoice_total < ANY
    (SELECT invoice_total
    FROM invoices
    WHERE vendor_id = 115);
    
/* EXISTS and NOT EXISTS */
SELECT vendor_id, vendor_name, vendor_state
FROM vendors
WHERE EXISTS
    (SELECT * FROM invoices WHERE vendor_id = vendors.vendor_id)
ORDER BY vendor_name ASC;

SELECT vendor_id, vendor_name, vendor_state
FROM vendors
WHERE NOT EXISTS
    (SELECT * FROM invoices WHERE vendor_id = vendors.vendor_id)
ORDER BY vendor_name ASC;