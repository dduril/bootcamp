# -----------------------------------------------
# Python Examples
#
# Lists
# -----------------------------------------------

def main():

    x = (1, 3, 5, 7, 9) # tuples are immutable and created with parenthesis
    print(type(x), x)

    x = [0, 2, 6, 8, 10] # lists are mutable and created with square brackets
    print(type(x), x)

    x.append(12)
    x.insert(2, 4)
    print(x)

    x = 'string' # string is a sequence type
    print(type(x), x)
    print(x[0])
    print(x[1])
    print(x[2])
    print(x[3])
    print(x[4])
    print(x[5])
    print(x[2:4])

    x = (1, 2, 3, 4, 5) # use sequence type as iterator
    for i in x:
        print(i)

    # same idea for strings
    s = "Hello"
    for i in s:
        print(i)

if __name__ == "__main__": main()
