# -----------------------------------------------
# Python Examples
#
# Files
# -----------------------------------------------

def main():
    try:
        fh = open('../raven.txt', 'r')
        for line in fh.readlines():
            print(line, end='')
    except IOError as e:
        print("Exception ({})".format(e))

if __name__ == "__main__": main()
