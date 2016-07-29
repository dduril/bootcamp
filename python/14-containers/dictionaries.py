# -----------------------------------------------
# Python Examples
#
# Dictionaries
# -----------------------------------------------

def main():
    d1 = dict(apple = 5, orange = 10, cherry = 12)
    print(type(d1))
    print(d1)
    print()

    d2 = dict(cashew = 4, walnut = 8, almond = 15)
    print(type(d2))
    print(d2)
    print()

    d3 = dict(carrot = 7, kale = 17, **d1)
    print(d3)
    print()

    print("'carrot' in d3? {}".format('carrot' in d3))
    print("'squash' in d3? {}".format('squash' in d3))
    print()

    for k in d3: print(k)
    print()

    for k, v in d3.items(): print(k, v)
    print()

    print(d1)
    print("d1 get 'apple': {}".format(d3.get('apple')))


if __name__ == "__main__": main()
