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

/* date formatting examples */
SELECT 
    invoice_date,
    DATE_FORMAT(invoice_date, '%m/%d/%y') AS 'm/d/y',
    DATE_FORMAT(invoice_date, '%W, %M %D, %Y') AS 'W, M D Y',
    DATE_FORMAT(invoice_date, '%e-%b-%y') AS 'e-b-y'
FROM invoices
WHERE invoice_date = '2014-08-02';

/* CASE examples */
SELECT invoice_number, terms_id,
    CASE terms_id
        WHEN 1 THEN 'Net due 10 days'
        WHEN 2 THEN 'Net due 20 days'
        WHEN 3 THEN 'Net due 30 days'
        WHEN 4 THEN 'Net due 60 days'
        WHEN 5 THEN 'Net due 90 days'
    END AS terms
FROM invoices
ORDER BY terms DESC;

SELECT invoice_number, invoice_total, invoice_date, invoice_due_date,
    CASE 
        WHEN DATEDIFF(DATE('2014-08-15'), invoice_due_date) > 30
            THEN 'Over 30 days past due'
        WHEN DATEDIFF(DATE('2014-08-15'), invoice_due_date) > 0
            THEN '1 to 30 days past due'
        ELSE 'Current'
    END AS invoice_status
FROM invoices
WHERE invoice_total - payment_total - credit_total > 0;


/* IF */
SELECT vendor_name, 
    IF(vendor_city = 'Fresno', 'Yes', 'No') AS is_city_fresno
FROM vendors;


/* IFNULL */
SELECT payment_date,
    IFNULL(payment_date, 'No Payment') AS new_date
FROM invoices;


/* COALESCE */
SELECT payment_date,
    COALESCE(payment_date, 'No Payment') AS new_date
FROM invoices;
