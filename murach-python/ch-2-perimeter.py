#!/usr/bin/env python3

# -------------------------------------
# Area and Perimeter Program
# Murach's Python Programming
# Chapter 2 Exercises
# -------------------------------------

# display a welcome message
print("The Area and Perimeter Program")
print()

# get input from the user
length= float(input("Please enter the length:\t"))
width = float(input("Please enter the width:\t"))

# calculate miles per gallon
area = length * width
perimeter = (2 * length) + (2 * width)

# format and display the result
print()
print("Area:\t\t" + str(area))
print("Perimeter:\t" + str(perimeter))
print()
print("Bye")