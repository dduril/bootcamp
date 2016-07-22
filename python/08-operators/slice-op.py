# -----------------------------------------------
# Python Examples
#
# Slice Operator
# -----------------------------------------------

def main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(list)

    # first element
    print("First element: {}".format(list[0]))

    # whole list
    print(list[:])

    # none of the list
    print(list[:0])

    # slice beginning at index 0 and then 5 items
    print(list[0:5])

if __name__ == "__main__": main()
