/*
 * ----------------------------------------------
 * MySQL Examples - Backing Up and Restoring a 
 *                  Database
 * ----------------------------------------------
 */
 
/* 
   -- MySQL bin directory for Windows
   
   cd /program files/mysql/mysql server 5.6/bin

   -- MySQL bin directory for Mac OS X and Unix/Linux

   cd /usr/local/mysql/bin
*/


/* Running the mysqldump program */
/*
-- for a single database
mysqldump movies > /development/mysql/movies-backup-11-07-2017.sql -u root -p

-- for specified databases
mysqldump --databases books movies sales mysql > /development/mysql/multiple-db-backup-11-07-2017.sql -u root -p

-- for all databases
mysqldump --all-databases > /development/mysql/all-db-backup-11-07-2017.sql -u root -p
*/


/* Using the mysql program to restore databases */
/*
-- for a single database
mysql movies < /development/mysql/movies-db-backup-11-07-2017.sql -u root -p

-- for multiple databases
mysql < /development/mysql/movies-db-backup-11-07-2017.sql -u root -p
*/


/* Using SELECT to export data to a file */
USE media;

-- tab-delimited file
SELECT *
INTO OUTFILE '/development/mysql/movie_tab.txt'
FROM movie;

-- comma-delimited file
SELECT *
INTO OUTFILE '/development/mysql/movie_comma.txt'
FIELDS TERMINATED BY ','
       ENCLOSED BY '"'
       ESCAPED BY '\\'    
FROM movie;


/* Using LOAD DATA to import data from a file */
USE ap;
TRUNCATE vendor_contacts;

LOAD DATA INFILE '/development/mysql/vendor_contacts_tab.txt'
INTO TABLE vendor_contacts;

SELECT * FROM vendor_contacts;
TRUNCATE vendor_contacts;

LOAD DATA INFILE '/development/mysql/vendor_contacts_comma.txt'
INTO TABLE vendor_contacts
FIELDS TERMINATED BY ','
       ENCLOSED BY '"'
       ESCAPED BY '\\';

SELECT * FROM vendor_contacts;


/* Using the CHECK TABLE statement */
USE ap;

-- checking a single table
CHECK TABLE vendors;
 
-- checking multiple tables and views
CHECK TABLE vendors, invoices, terms, invoices_outstanding;
 
-- using an option
CHECK TABLE vendors, invoices FAST;

/* Using the REPAIR TABLE statement */

USE ap;

-- repairing a single table
REPAIR TABLE vendors;

-- repairing two tables and using an option
REPAIR TABLE vendors, invoices QUICK;
