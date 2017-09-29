/*
 * ----------------------------------------------
 * MySQL Examples - Triggers and Events
 * ----------------------------------------------
 */
 
USE ap;

-- test vendors_before_update
-- ..............................................................
UPDATE vendors
SET vendor_state = 'wi'
WHERE vendor_id = 1;

SELECT vendor_name, vendor_state
FROM vendors
WHERE vendor_id = 1;


-- test invoices_before_update
-- ..............................................................
UPDATE invoices
SET invoice_total = 600
WHERE invoice_id = 100;

SELECT invoice_id, invoice_total, credit_total, payment_total 
FROM invoices WHERE invoice_id = 100;


-- test invoices_audit, invoices_after_insert, invoices_after_delete
-- ..............................................................
-- make sure that there is at least one record to delete
INSERT INTO invoices VALUES 
(115, 34, 'ZXA-080', '2014-08-30', 14092.59, 0, 0, 3, '2014-09-30', NULL);

DELETE FROM invoices WHERE invoice_id = 115;

SELECT * FROM invoices_audit;

-- clean up
-- DELETE FROM invoices_audit;


-- test TRIGGERS
-- ..............................................................
SHOW TRIGGERS;
SHOW TRIGGERS IN ex;
SHOW TRIGGERS IN ap LIKE 'ven%';

-- DROP TRIGGER vendors_before_update;
-- DROP TRIGGER IF EXISTS vendors_before_update;


-- test EVENTS
-- ..............................................................
SHOW VARIABLES LIKE 'event_scheduler';
SHOW EVENTS;
SHOW EVENTS IN ap;