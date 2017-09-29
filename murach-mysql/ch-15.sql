/*
 * ------------------------------------------------
 * MySQL Examples - Stored Procedures and Functions
 * ------------------------------------------------
 */
 
USE ap;

-- test insert_invoice
-- ..............................................................
CALL insert_invoice(34, 'ZXA-080', '2015-01-18', 14092.59, 
                    3, '2015-03-18');
CALL insert_invoice(34, 'ZXA-082', '2015-01-18', 14092.59,
                    NULL, NULL);

-- this statement raises an error
CALL insert_invoice(34, 'ZXA-083', '2015-01-18', -14092.59,
                    NULL, NULL);

-- clean up
SELECT * FROM invoices WHERE invoice_id >= 115;

-- DELETE FROM invoices WHERE invoice_id >= 115;


-- test select_invoices
-- ..............................................................
CALL select_invoices('2014-07-25', 100);

CALL select_invoices('2014-07-25', NULL);

CALL select_invoices(NULL, 1000);

CALL select_invoices(NULL, NULL);


-- test get_vendor_id
-- ..............................................................
SELECT invoice_number, invoice_total
FROM invoices
WHERE vendor_id = get_vendor_id('IBM');


-- test get_balance_due
-- ..............................................................
SELECT vendor_id, invoice_number, 
       get_balance_due(invoice_id) AS balance_due 
FROM invoices
WHERE vendor_id = 37;


-- test get_balance_due, get_sum_balance_due
-- ..............................................................
SELECT vendor_id, invoice_number, 
       get_balance_due(invoice_id) AS balance_due, 
       get_sum_balance_due(vendor_id) AS sum_balance_due
FROM invoices
WHERE vendor_id = 37;

-- DROP FUNCTION get_sum_balance_due;


