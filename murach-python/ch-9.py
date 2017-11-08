# -------------------------------------
# Chapter 9 Code Examples
#   Working with Numbers
# -------------------------------------

# import the locale and math modules
import locale as lc
import math as m

# example with floating-point error
balance = 100.10
balance += 100.10
balance += 100.10
print("Balance: ", balance) # Balance:  300.29999999999995 (floating-point error)

# fixing the floating-point error
balance = round(balance, 2)
print("Balance: ", balance)

# using the pow() and sqrt() functions
result = m.pow(2, 3)
print("Result: ", result)

result = m.sqrt(25)
print("Result: ", result)

result = m.pow(125, 1/3)
print("Result: ", result, "\n")

# using the pi constant
radius = 12
circumference = m.pi * radius * 2
area = m.pi * m.pow(radius, 2)
area = m.pi * radius**2

# using the floor() and ceil() functions
result = m.floor(12.545)
print("Result: ", result)
result = m.ceil(12.545)
print("Result: ", result)
result = m.floor(-3.432)
print("Result: ", result)
result = m.ceil(-3.432)
print("Result: ", result, "\n")

# using the ceil() function with decimal places
print(m.ceil(2.0083))
print(m.ceil(2.0083 * 10) / 10)
print(m.ceil(2.0083 * 100)/ 100, "\n")

# using the floor() function with decimal places
print(m.floor(2.0083))
print(m.floor(2.0083 * 10) / 10)
print(m.floor(2.0083 * 1000)/ 1000, "\n")

# formatting numbers
fp_number = 1234.5678
print("{:.2f}".format(fp_number))
print("{:.4f}".format(fp_number))
print("{:,.2f}".format(fp_number))
print("{:10,.2f}".format(fp_number), "\n")

int_number = 12345
print("{:d}".format(int_number))
print("{:,d}".format(int_number), "\n")

fp_number = .12345
print("{:.0%}".format(fp_number))
print("{:.1%}".format(fp_number), "\n")

fp_number = 12345.6789
print("{:.2e}".format(fp_number))
print("{:.4e}".format(fp_number), "\n")

# set the locale to English/United States
lc.setlocale(lc.LC_ALL, "us")
print(lc.currency(12345.25, grouping=True))
print(lc.format("%d", 12345, grouping=True))
print(lc.format("%.2f", 12345.45, grouping=True))
