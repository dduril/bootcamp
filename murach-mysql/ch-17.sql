/*
 * ----------------------------------------------
 * MySQL Examples - Database Administration
 * ----------------------------------------------
 */
 
-- base and data directories for Windows
-- C:\Program Files\MySQL\MySQL Server 5.6
-- C:\Program Files\MySQL\MySQL Server 5.6\data

-- base and data directories for Mac OS X and Unix/Linux
-- usr/local/mysql/
-- usr/local/mysql/data


-- examples of setting system variables
SET GLOBAL  autocommit = ON;
SET SESSION autocommit = OFF;
SET GLOBAL  autocommit = DEFAULT;

SET GLOBAL  max_connections = 90;
SET GLOBAL  max_connections = DEFAULT;

SET GLOBAL  tmp_table_size = 36700160;
SET GLOBAL  tmp_table_size = 35 * 1024 * 1024;


-- examples of getting system variables
SELECT @@GLOBAL.autocommit, @@SESSION.autocommit;
SELECT @@GLOBAL.max_connections, @@GLOBAL.tmp_table_size;


-- reset values
SET SESSION autocommit = DEFAULT;
SET GLOBAL  tmp_table_size = DEFAULT;


-- logging options set in the server configuration file
general_log
general_log_file = "/development/mysql/general.log"

log_error = "/development/mysql/error.log"

log_bin = "/development/mysql/bin-log"

slow_query_log
slow_query_log_file = "/development/mysql/slow.log"

-- viewing log files when they are written to tables
SELECT * FROM mysql.general_log;

SELECT * FROM mysql.slow_log;