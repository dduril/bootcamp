/*
 * ----------------------------------------------
 * MySQL Examples - INSERT, UPDATE, and DELETE
 *                  Statements
 * ----------------------------------------------
 */

/* create a copy of a table using CREATE TABLE AS */
CREATE TABLE invoices_copy AS
SELECT * FROM invoices;

CREATE TABLE old_invoices AS
SELECT * FROM invoices
WHERE invoice_total - payment_total - credit_total = 0;

CREATE TABLE vendor_balances AS
SELECT 
    vendor_id, 
    SUM(invoice_total) AS sum_of_invoices
FROM invoices
    WHERE (invoice_total - payment_total - credit_total) <> 0
GROUP BY vendor_id;

DROP TABLE old_invoices;

/* INSERT examples */
/* without column list */
INSERT INTO invoices VALUES
(115, 97, '456789', '2014-08-01', 8344.50, 0, 0, 1, '2014-08-31', NULL);

/* with column list */
INSERT INTO invoices
    (vendor_id, invoice_number, invoice_total, terms_id, invoice_date, 
     invoice_due_date)
VALUES
    (97, '456789', 8344.50, 1, '2014-08-01', '2014-08-31');    
    
/* multiple rows */
INSERT INTO invoices VALUES
(116, 97, '456701', '2014-08-02', 270.50, 0, 0, 1, '2014-09-01', NULL),
(117, 97, '456791', '2014-08-03', 4390.00, 0, 0, 1, '2014-09-02', NULL),
(118, 97, '456792', '2014-08-03', 565.60, 0, 0, 1, '2014-09-02', NULL);

/* INSERT examples using default and null values */
USE media_db;

INSERT INTO movies (movie_id)
VALUES (100);

INSERT INTO movies (movie_name)
VALUES ('Star Wars');

INSERT INTO movies
VALUES (DEFAULT, DEFAULT, 'Star Wars');

INSERT INTO movies
VALUES (DEFAULT, 100, NULL);

INSERT INTO movies
VALUES (DEFAULT, DEFAULT, NULL);

/* INSERT with subquery */
INSERT INTO invoice_archive
SELECT *
FROM invoices
WHERE invoice_total - payment_total - credit_total = 0;

INSERT INTO invoice_archive
    (invoice_id, vendor_id, invoice_number, invoice_total, credit_total,
    payment_total, terms_id, invoice_date, invoice_due_date)
SELECT
    invoice_id, vendor_id, invoice_number, invoice_total, credit_total, 
    payment_total, terms_id, invoice_date, invoice_due_date
FROM invoices
WHERE invoice_total - payment_total - credit_total = 0;

/* UPDATE examples */
UPDATE invoices
SET payment_date = '2014-09-21', 
    payment_total = 19351.18
WHERE invoice_number = '97/522';

UPDATE invoices
SET terms_id = 1
WHERE vendor_id = 95;

UPDATE invoices
SET credit_total = credit_total + 100
WHERE invoice_number = '97/522';

UPDATE invoices
SET terms_id = 1
WHERE vendor_id =
   (SELECT vendor_id
    FROM vendors
    WHERE vendor_name = 'Pacific Bell');
    
UPDATE invoices
SET terms_id = 1
WHERE vendor_id IN
   (SELECT vendor_id
    FROM vendors
    WHERE vendor_state IN ('CA', 'AZ', 'NV'));
    
/* DELETE examples */   
DELETE FROM general_ledger_accounts
WHERE account_number = 306;

DELETE FROM invoice_line_items
WHERE invoice_id = 78 AND invoice_sequence = 2;

DELETE FROM invoice_line_items
WHERE invoice_id = 12;

DELETE FROM invoice_line_items
WHERE invoice_id IN
    (SELECT invoice_id
     FROM invoices
     WHERE vendor_id = 115);