# -------------------------------------
# Chapter 13 Code Examples
#   Recursion and Algorithms
# -------------------------------------


# iterative function that sums all numbers from zero to an upper limit
def add_numbers_iterative(upper):
    total = 0
    for number in range(upper + 1):
        total += number
    return total


# recursive function that sums all numbers from zero to an upper limit
def add_numbers_recursive(upper):
    if upper == 0:
        return upper
    else:
        return upper + add_numbers_recursive(upper - 1)


# recursive function that calculates the factorial of a number
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


# recursive function that calculates a Fibonacci series
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


x = add_numbers_iterative(5)
print("add_numbers_iterative(5) : " + str(x))

x = add_numbers_recursive(5)
print("add_numbers_recursive(5) : " + str(x))

x = factorial(5)
print("factorial(5) : " + str(x))

for i in range(20):
    print(fib(i), end=" ")
