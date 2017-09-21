/*
 * ----------------------------------------------
 * MySQL Examples - Data Types
 * ----------------------------------------------
 */

 /* CONCAT $ to invoice_total */
SELECT 
    invoice_date,
    invoice_number,
    CONCAT('$', invoice_total) as invoice_total
FROM invoices
ORDER BY invoice_date DESC;

/* CONCAT full vendor name and address */
SELECT CONCAT(vendor_name, ', ', vendor_address1, ', ',
       vendor_city, ', ', vendor_state, ' ', vendor_zip_code)
       AS vendor_full_address
FROM vendors
WHERE vendor_name LIKE 'A%'
ORDER BY vendor_name;