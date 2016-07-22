# -----------------------------------------------
# Python Examples
#
# Variable Identities
# -----------------------------------------------

def main():
    x = 100
    print(id(x))
    print(type(x), x)

    y = 100
    print(id(y))
    print(type(y), y)

    # print(x==y)
    if x == y:
        print(True)
    else:
        print(False)

if __name__ == "__main__": main()
