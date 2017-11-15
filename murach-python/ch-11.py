# -------------------------------------
# Chapter 11 Code Examples
#   Working with Dates and Times
# -------------------------------------

from datetime import date
from datetime import time
from datetime import datetime

current_date = date.today()
print(current_date)

invoice_date = datetime.now()
print(invoice_date)

appointment = datetime(2017, 11, 20, 8, 30)
print(appointment)

# using strptime (parse)
dt = datetime.strptime("11/15/2017 9:30:45", "%m/%d/%Y %H:%M:%S")
print(dt)

# using strftime (format)
