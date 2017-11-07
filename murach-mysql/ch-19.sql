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