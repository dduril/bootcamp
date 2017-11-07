/*
 * ----------------------------------------------
 * MySQL Examples - Securing a Database
 * ----------------------------------------------
 */
 
/* script to create 2 users and grant privileges */
DROP USER ap_admin@localhost;
DROP USER ap_user@localhost;

CREATE USER ap_admin@localhost IDENTIFIED BY 'pa55word';
CREATE USER ap_user@localhost IDENTIFIED BY 'pa55word';

GRANT ALL
ON ap.*
TO ap_admin@localhost;

GRANT SELECT, INSERT, DELETE, UPDATE
ON ap.*
TO ap_user@localhost;

/* view the privileges for these users */
SHOW GRANTS FOR ap_admin@localhost;

/* Privileges for working with data

   SELECT
   INSERT
   UPDATE
   DELETE
   EXECUTE
   
   Privileges for modifying the database structure
   
   CREATE
   ALTER
   DROP
   INDEX
   CREATE VIEWS
   CREATE ROUTINE
   ALTER ROUTINE
   TRIGGER
   EVENT
   
   Administrative Privileges
   
   CREATE USER
   RELOAD
   SHOW DATABASES
   SHUTDOWN
   
   Other Privileges
   
   ALL
   GRANT OPTION
   USAGE
   
   List of grant tables in the mysql database
   
   user
   db
   tables_priv
   columns_priv
   procs_priv
 
*/

/* Users and Privileges Example */
DROP USER john@localhost;
DROP USER jane;

CREATE USER john@localhost IDENTIFIED BY 'sesame';
CREATE USER jane IDENTIFIED BY 'sesame';    -- creates jane@%

RENAME USER john@localhost TO johnsmith@localhost;

DROP USER johnsmith@localhost;
DROP USER jane;                             -- drops jane@%

/* Granting Privileges Examples */
GRANT USAGE
ON *.*
TO john@localhost IDENTIFIED BY 'sesame';

GRANT ALL 
ON *.*
TO jim IDENTIFIED BY 'supersecret'
WITH GRANT OPTION;

GRANT SELECT, INSERT, UPDATE, DELETE
ON ap.*
TO ap_user@localhost IDENTIFIED BY 'pa55word';

GRANT SELECT, INSERT, UPDATE
ON *.* TO ap_user@localhost;

GRANT SELECT, INSERT, UPDATE
ON ap.* TO john@localhost;

GRANT SELECT, INSERT, UPDATE
ON ap.vendors TO john@localhost;

GRANT SELECT (vendor_name, vendor_state, vendor_zip_code), 
      UPDATE (vendor_address1)
ON ap.vendors TO john@localhost;

GRANT SELECT, INSERT, UPDATE, DELETE
ON vendors TO ap_user@localhost;

/* Viewing Privileges Examples */
SELECT User, Host FROM mysql.user;
 
SHOW GRANTS FOR jim;
SHOW GRANTS FOR ap_user@localhost;
SHOW GRANTS;

/* Revoking Privileges Examples */
REVOKE ALL, GRANT OPTION 
FROM jim;

REVOKE ALL, GRANT OPTION 
FROM ap_admin, john@localhost;

REVOKE UPDATE, DELETE
ON ap.invoices FROM john@localhost

/* Changing Passwords Examples */
SET PASSWORD FOR john = PASSWORD('pa55word');

SET PASSWORD = PASSWORD('secret');

GRANT USAGE ON *.* TO john IDENTIFIED BY 'pa55word';

SELECT Host, User
FROM mysql.user
WHERE Password = '';

/* Full Script for Creating Users */
-- drop the users (causes an error if they don't exist yet)
DROP USER john;
DROP USER jane;
DROP USER jim;
DROP USER john@localhost;

-- create the users
CREATE USER john IDENTIFIED BY 'sesame';
CREATE USER jane IDENTIFIED BY 'sesame';
CREATE USER jim IDENTIFIED BY 'sesame';
CREATE USER john@localhost IDENTIFIED BY 'sesame';

-- grant privileges to the ap_developer (john)
GRANT ALL ON *.* TO john@localhost WITH GRANT OPTION;

-- grant privileges to the ap manager (jim)
GRANT SELECT, INSERT, UPDATE, DELETE ON ap.* TO jim;
GRANT USAGE ON ap.* TO jim WITH GRANT OPTION;

-- grant privileges to ap users (john, jane)
GRANT SELECT, INSERT, UPDATE, DELETE ON ap.vendors TO john, jane;
GRANT SELECT, INSERT, UPDATE, DELETE ON ap.invoices TO john, jane;
GRANT SELECT, INSERT, UPDATE, DELETE ON ap.invoice_line_items TO john, jane;
GRANT SELECT ON ap.general_ledger_accounts TO john, jane;
GRANT SELECT ON ap.terms TO john, jane;

-- view user account data
SELECT User, Host, Password FROM mysql.user;

-- view the privileges for each user
SHOW GRANTS FOR john;
SHOW GRANTS FOR jane;
SHOW GRANTS FOR jim;
SHOW GRANTS FOR john@localhost;
