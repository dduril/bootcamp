# -----------------------------------------------
# Python Examples
#
# Functions
# -----------------------------------------------

def main():
    greeting()
    greeting('John')
    listStuff(10, 20, 30, 40, 50)

def greeting(name='World!'):
    print("Hello", name)

def listStuff(x, y, *args):
    print(x, y)
    for n in args: print(n, end=' ')

if __name__ == "__main__": main()
