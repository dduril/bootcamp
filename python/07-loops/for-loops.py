# -----------------------------------------------
# Python Examples
#
# For Loops - Iterators
# -----------------------------------------------

def main():
    fh = open("raven.txt")
    for line in fh.readlines():
        print(line, end='')

if __name__ == "__main__": main()
