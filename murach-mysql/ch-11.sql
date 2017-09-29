/*
 * ----------------------------------------------
 * MySQL Examples - Creating Databases, Tables,
 *                  and Indexes
 * ----------------------------------------------
 */
 
-- CREATE DATABASE examples
CREATE DATABASE ap;

CREATE DATABASE IF NOT EXISTS ap;

DROP DATABASE ap;

DROP DATABASE IF EXISTS ap;


-- USE database example
USE ap;


-- CREATE TABLE examples
CREATE TABLE vendors
(
  vendor_id     INT            NOT NULL    UNIQUE AUTO_INCREMENT,
  vendor_name   VARCHAR(50)    NOT NULL    UNIQUE
);

CREATE TABLE invoices
(
  invoice_id       INT            NOT NULL    UNIQUE,
  vendor_id        INT            NOT NULL,
  invoice_number   VARCHAR(50)    NOT NULL,
  invoice_date     DATE,
  invoice_total    DECIMAL(9,2)   NOT NULL,
  payment_total    DECIMAL(9,2)               DEFAULT 0
)


-- ALTER TABLE examples
ALTER TABLE vendors
ADD last_transaction_date DATE;

ALTER TABLE vendors
DROP COLUMN last_transaction_date;

ALTER TABLE vendors
MODIFY vendor_name VARCHAR(100) NOT NULL DEFAULT 'New Vendor';

ALTER TABLE vendors
ADD PRIMARY KEY (vendor_id);

ALTER TABLE invoices
ADD CONSTRAINT invoices_fk_vendors
FOREIGN KEY (vendor_id) REFERENCES vendors (vendor_id);

ALTER TABLE vendors
DROP PRIMARY KEY;

ALTER TABLE invoices
DROP FOREIGN KEY invoices_fk_vendors;


-- CREATE INDEX examples
CREATE INDEX invoices_invoice_date_ix
  ON invoices (invoice_date);
  
CREATE INDEX invoices_vendor_id_invoice_number_ix
  ON invoices (vendor_id, invoice_number);
  
CREATE UNIQUE INDEX vendors_vendor_phone_ix
  ON vendors (vendor_phone);
  
CREATE INDEX invoices_invoice_total_ix
  ON invoices (invoice_total DESC);
  
DROP INDEX vendors_vendor_phone_ix ON vendors;


-- RENAME, TRUNCATE, DROP
RENAME TABLE vendors TO vendor;

TRUNCATE TABLE vendor;

DROP TABLE vendor;


-- SHOW properties examples
SHOW CHARSET;

SHOW CHARSET LIKE 'latin1';

SHOW COLLATION;

SHOW COLLATION LIKE 'latin1%';

SHOW VARIABLES LIKE 'character_set_server';

SHOW VARIABLES LIKE 'collation_server';

SHOW VARIABLES LIKE 'character_set_database';

SHOW VARIABLES LIKE 'collation_database';

SHOW VARIABLES LIKE 'storage_engine';

SELECT table_name, engine
FROM information_schema.tables
WHERE table_schema = 'ap';