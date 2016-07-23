# -----------------------------------------------
# Python Examples
#
# Handling Exceptions
# -----------------------------------------------

def main():
    try:
        fh = open('../x-raven.txt') # file does not exist
        for line in fh.readlines():
            print(line, end='')
    except IOError as e:
        print("Exception ({})".format(e))

if __name__ == "__main__": main()
