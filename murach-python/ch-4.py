# -------------------------------------
# Chapter 4 Code Examples
# -------------------------------------

import random


# function examples
def print_hello():
    print("Hello")
    print()

print_hello()


def print_hello_name(name):
    print("Hello " + name)
    print()

print_hello_name("John")


def add_numbers(x, y):
    total = x + y
    return total

a = 10
b = 20
t = add_numbers(a, b)


# main() function
def main():
    print("Welcome to the Employee Management System")
    print()

# if statement that checks that the current module is being run as the main module
if __name__ == "__main__":
    main()


# simple function examples
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

f = 80
c = 20
print(f, "Fahrenheit = ", round(convert_to_celsius(f)), "Celsius")
print(c, "Celsius = ", round(convert_to_fahrenheit(c)), "Fahrenheit")


# random numbers
number1 = random.random()                # float >= 0.0 and < 1.0
number2 = random.random() * 100          # float >= 0.0 and < 100.0

number3 = random.randint(1, 25)          # int from 1 to 25
number4 = random.randint(0, 10)           # int from 0 10 10

number5 = random.randrange(1, 100)       # int from 1 to 99
number6 = random.randrange(0, 50, 2)     # even int from 0 to 50
number7 = random.randrange(1, 50, 1)     # odd int from 1 to 50

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
print("Roll the dice: ", die1, die2)
