/*
 * ----------------------------------------------
 * MySQL Examples - Functions
 * ----------------------------------------------
 */

/* other available functions
    LOWER(vendor_name),
    UPPER(vendor_name),
    REVERSE(vendor_name),
    LENGTH(vendor_name),
    LTRIM(vendor_name),
    RTRIM(vendor_name),
    TRIM(vendor_name),
*/
SELECT 
    vendor_name,

    CONCAT_WS(', ', vendor_contact_last_name, 
        vendor_contact_first_name) AS contact_name,
    LEFT(vendor_phone, 5) AS area_code,
    RIGHT(vendor_phone, 8) AS phone 
FROM vendors
WHERE LEFT(vendor_phone, 4) = '(559'
ORDER BY contact_name;

/* date parsing functions */
SELECT 
    invoice_date,
    YEAR(invoice_date) AS year,
    MONTH(invoice_date) AS month,
    DAYOFMONTH(invoice_date) AS day_of_month,
    DAYOFWEEK(invoice_date) AS day_of_week,
    QUARTER(invoice_date) AS quarter,
    DAYOFYEAR(invoice_date) AS day_of_year,
    DAYNAME(invoice_date) AS day_name,
    MONTHNAME(invoice_date) AS month_name
FROM invoices
WHERE invoice_date = '2014-08-02';