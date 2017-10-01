# -------------------------------------
# Chapter 8 Code Examples
#   Exception Handling
# -------------------------------------

# handle ValueError exception
try:
    number = int(input("Enter an integer: "))
    print("You entered a valid integer: " + str(number) + ".")
except ValueError:
    print("You entered an invalid integer. Please try again.")

# handle all exceptions
try:
    number = int(input("Enter an integer: "))
    print("You entered a valid integer: " + str(number) + ".")
except:
    print("You entered an invalid integer. Please try again.")

# handling multiple exceptions
filename = input("Enter filename: ")
movies = []
try:
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
except FileNotFoundError:
    print("File not found: " + filename)
except OSError:
    print("File found. Error reading file.")
except Exception:
    print("An unexpected error has occurred.")

# handling multiple exceptions using type() and exit()

# import the sys module
import sys


