# -----------------------------------------------
# Python Examples
#
# Enumerating Iterators
# -----------------------------------------------

def main():
    fh = open("raven.txt")
    for index, line in enumerate(fh.readlines()):
        print(index, line, end='')

    print("\n\n")

    s = "Hello World!"
    for i, c in enumerate(s):
        print(i, c)

if __name__ == "__main__": main()
