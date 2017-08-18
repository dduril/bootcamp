#!/usr/bin/env python3

# -------------------------------------
# Miles Per Gallon Program
# Murach's Python Programming
# Chapter 2 Exercises
# -------------------------------------

# display a welcome message
print("The Miles Per Gallon Program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 1)
total_gas_cost = round(gallons_used * cost_per_gallon, 1)
cost_per_mile = round(total_gas_cost / miles_driven, 1)

# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total Gas Cost:\t\t\t" + str(total_gas_cost))
print("Cost Per Mile:\t\t\t" + str(cost_per_mile))
print()
print("Bye")