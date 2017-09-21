/*
 * ----------------------------------------------
 * MySQL Examples - Summary Queries
 * ----------------------------------------------
 */

/* using aggregate functions */
SELECT
    COUNT(*) AS number_of_invoices,
    SUM(invoice_total - payment_total - credit_total) AS total_due
FROM invoices
WHERE invoice_total - payment_total - credit_total > 0;

/* using COUNT(*), AVG, SUM */
SELECT
    'After 1/1/2014' AS selection_date,
    COUNT(*) AS number_of_invoices,
    ROUND(AVG(invoice_total), 2) AS average_invoice_amount,
    SUM(invoice_total) AS total_invoice_amount
FROM invoices
WHERE invoice_date > '2014-01-01';

/* using MIN and MAX */
SELECT
    'After 1/1/2014' AS selection_date,
    COUNT(*) AS number_of_invoices,
    MIN(invoice_total) AS lowest_invoice_total,
    MAX(invoice_total) AS highest_invoice_total
FROM invoices
WHERE invoice_date > '2014-01-01';

/* using DISTINCT */
SELECT
    COUNT(DISTINCT vendor_id) AS number_of_vendors,
    COUNT(vendor_id) AS number_of_invoices,
    ROUND(AVG(invoice_total), 2) AS average_invoice_amount,
    SUM(invoice_total) AS total_invoice_amount
FROM invoices
WHERE invoice_date > '2014-01-01';

/* using GROUP BY and HAVING */
SELECT 
    vendor_id,
    ROUND(AVG(invoice_total), 2) AS average_invoice_amount
FROM invoices
GROUP BY vendor_id
HAVING AVG(invoice_total) > 2000
ORDER BY average_invoice_amount DESC;

SELECT 
    vendor_id,
    COUNT(*) AS invoice_qty
FROM invoices
GROUP BY vendor_id;

SELECT 
    v.vendor_state,
    v.vendor_city,
    COUNT(*) AS invoice_qty,
    ROUND(AVG(i.invoice_total), 2) AS invoice_avg
FROM invoices i JOIN vendors v
    ON i.vendor_id = v.vendor_id
GROUP BY v.vendor_state, v.vendor_city;

SELECT
    invoice_date,
    COUNT(*) AS invoice_qty,
    SUM(invoice_total) AS invoice_sum
FROM invoices
    WHERE invoice_date BETWEEN '2014-05-01' AND '2014-05-31'
GROUP BY invoice_date
HAVING COUNT(*) > 1 AND SUM(invoice_total) > 100
ORDER BY invoice_date DESC;