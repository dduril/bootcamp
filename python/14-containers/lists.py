# -----------------------------------------------
# Python Examples
#
# Tuples, Lists
# -----------------------------------------------

def main():

    # tuple - immutable
    tpl = (2, 4, 6, 8, 10, 4, 4, 4, 4)
    print("type:\t{}".format(type(tpl)))
    print("tuple:\t{}".format(tpl))
    print("length:\t{}".format(len(tpl)))
    print("min:\t{}".format(min(tpl)))
    print("max:\t{}".format(max(tpl)))
    print("# 4s:\t{}".format(tpl.count(4)))
    print()

    # list - mutable
    lst = [5, 10, 15, 20, 25, 30, 35, 40]
    print("type:\t{}".format(type(lst)))
    print("list:\t{}".format(lst))
    print("length:\t{}".format(len(lst)))
    print("min:\t{}".format(min(lst)))
    print("max:\t{}".format(max(lst)))
    lst[3] = 100 # modify list
    lst.append(150) # append value to list
    lst.insert(0, 200) # insert to beginning of list
    print(lst)
    print()

    # more tuple examples
    t = tuple(range(25))
    print(type(t))
    print(t)
    print("10 in t? {}".format(10 in t))
    print("25 in t? {}".format(25 in t))
    for i in t: print(i)


if __name__ == "__main__": main()
