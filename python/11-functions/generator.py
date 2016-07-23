# -----------------------------------------------
# Python Examples
#
# Generators
# -----------------------------------------------

def main():
    for i in inclusive_range(25):
        print(i, end=' ')
    print('\n')
    for i in inclusive_range(15, 25):
        print(i, end=' ')
    print('\n')
    for i in inclusive_range(5, 100, 5):
        print(i, end=' ')

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('Requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('inclusive_range expects at most 3 arguments, received {}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == "__main__": main()
