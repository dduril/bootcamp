# -------------------------------------
# Chapter 2 Code Examples
#   Basics
# -------------------------------------

# script with 3 statements
print("Hello Python!")
print()
print("Bye!")

# initialize variables and assign values
product_name = "Toaster"
quantity1 = 25
quantity2 = 42
list_price = 10.99

# naming conventions for variables
product_code = 1       # underscore notation
productCode = 2        # camel case

# another example
department_name = "Accounting"
departmentName = "Accounting"

# code that calculates sales tax
subtotal = 100.00
tax_percent = .08
tax_amount = subtotal * tax_percent
grand_total = subtotal + tax_amount

# code that calculates the perimeter of a rectangle
width = 5.25
length = 10.75
perimeter = (2 * width) + (2 * length)

# ways to increment a variable
counter = 0
counter = counter + 1
counter += 1

# assigning strings to variables
first_name = "John"
last_name = "Smith"
full_name = "John Smith"

# concatenating strings together
name = first_name + " " + last_name

# joining a string with a number
age = 42
message = name + " is " + str(age) + " years old."

# implicit continuation of a string over several lines
score_total = 370
average_score = 92.5
print("Total Score: "
      + str(score_total)
      + "\nAverage Score: "
      + str(average_score))

# new line character
print("Title: Python Programming\nPublished: 2017")

# tab and new line characters
print("Title:\t\tPython Programming\nPublished:\t2017")

# backslash in a Windows path
print("C:\\development\\python\\io\\examples")

# print() function examples
print(19.99)
print("Price", 19.99)
print(1, 2, 3, 4, 5, 6, 7, 8)
print("Total Score:", score_total, "\nAverage Score:", average_score)
print("Total Score: " + str(score_total) + "\nAverage Score: " + str(average_score))
print(1, 2, 3, 4, 5, 6, 7, 8, sep=' | ')
print(1, 2, 3, 4, 5, 6, 7, 8, end='Done')

# getting string input from a user
first_name = input("Enter your first name: ")
last_name = input("enter you last name: ")
print("Hello " + first_name + " " + last_name + ".")

# getting int or float input from a user
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))

# using the round() function
miles_driven = 150
gallons_used = 5.875
mpg = round(miles_driven / gallons_used, 2)
