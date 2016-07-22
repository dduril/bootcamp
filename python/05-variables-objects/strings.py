# -----------------------------------------------
# Python Examples
#
# Strings
# -----------------------------------------------

def main():
    s = "Hello World!"
    print(type(s), s)

    s = "Hello\nWorld!"
    print(s)

    s = r"Hello\nWorld!"    # raw string
    print(s)

    n = 48
    s = "This is a {} string".format(n)
    print(s)

    s = '''\
This is a triple-quoted string
and can span multiple lines
''' # can also use triple-double quotes
    print(s)

if __name__ == "__main__": main()
