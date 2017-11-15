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
holiday_brunch = datetime(2017, 11, 23, 8, 30)
holiday_lunch = datetime(2017, 11, 23, 14, 0)

print("Thanksgiving Brunch: " + holiday_brunch.strftime("%Y-%m-%d (%A) at %I:%M %p"))
print("Thanksgiving Lunch: " + holiday_lunch.strftime("%Y-%m-%d (%A) at %I:%M %p") + "\n")
print("Thanksgiving Lunch: " + holiday_lunch.strftime("%c"))
print("Thanksgiving Lunch: " + holiday_lunch.strftime("%x (%B, %A)"))
print("\n")

# returning parts of a date/time object
thanksgiving = datetime(2017, 11, 23, 15, 30, 0)
year = thanksgiving.year
month = thanksgiving.month
day = thanksgiving.day
hour = thanksgiving.hour
minute = thanksgiving.minute
second = thanksgiving.second
microsecond = thanksgiving.microsecond
print(year, month, day, hour, minute, second, microsecond)
