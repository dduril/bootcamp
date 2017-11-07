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
