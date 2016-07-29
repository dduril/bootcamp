# -----------------------------------------------
# Python Examples
#
# Strings
# -----------------------------------------------

def main():
    str = "Hello World!"
    print(type(str))
    print("id():\t\t\t{}".format(id(str)))
    print("str:\t\t\t{}".format(str))
    print("lower():\t\t{}".format(str.lower()))
    print("upper():\t\t{}".format(str.upper()))
    print("capitalize():\t{}".format(str.capitalize()))
    print("title():\t\t{}".format(str.title()))
    print("swapcase():\t\t{}".format(str.swapcase()))
    print("len(str):\t\t{}".format(len(str)))
    print()

    str = "A long time ago in a galaxy far far away..."
    print(str)
    print(str.split())

    words = str.split()
    for w in words: print(w)

    new = ":".join(words)
    print(new)
    print()

    x, y, = "10", "20"
    print("x: {}, y: {}".format(x, y))
    print(x.isalpha())
    print(x.isalnum())
    print(x.isnumeric())

if __name__ == "__main__": main()
