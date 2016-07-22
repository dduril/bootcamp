# -----------------------------------------------
# Python Examples
#
# Dictionary
# -----------------------------------------------

def main():
    d = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }
    print(type(d), d)

    for k in d:
        print(k, d[k]) # output not in any order

    for k in sorted(d.keys()):
        print(k, d[k]) # alphabetical order


    d = dict(
        apples = 5, bananas = 7, cherries = 10, oranges = 8, pears = 4
    )
    d['kiwis'] = 14
    d['grapes'] = 9
    for k in sorted(d.keys()):
        print(k, d[k])

if __name__ == "__main__": main()
