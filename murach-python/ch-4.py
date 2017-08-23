# -------------------------------------
# Chapter 4 Code Examples
# -------------------------------------


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
