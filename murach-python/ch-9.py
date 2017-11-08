# -------------------------------------
# Chapter 9 Code Examples
#   Working with Numbers
# -------------------------------------

# import the math module
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
print(m.floor(2.0083 * 1000)/ 1000)

