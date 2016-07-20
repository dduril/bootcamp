# -----------------------------------------------
# Python Examples
#
# Functions
# -----------------------------------------------

def main():
    func1()     # no arguments for func1
    func2(5)    # start range at 5
    func3()     # use default argument, start range at 1

def func1():
    for i in range(20): # print 0 - 19
        print(i, end=' ')
    print()

def func2(n):
    for i in range(n, 20):
        print(i, end=' ')
    print()

def func3(n = 1):
    for i in range(n, 20):
        print(i, end=' ')
    print()

if __name__ == "__main__": main()
