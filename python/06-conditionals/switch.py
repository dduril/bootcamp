# -----------------------------------------------
# Python Examples
#
# Switch
# -----------------------------------------------

def main():
    options = dict(
        one = 'pepperoni',
        two = 'sausage',
        three = 'black olives',
        four = 'mushrooms',
        five = 'extra cheese'
    )
    v = 'calamari'
    print(options.get(v, 'other'))

if __name__ == "__main__": main()
