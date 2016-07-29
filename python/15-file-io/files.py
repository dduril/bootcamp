# -----------------------------------------------
# Python Examples
#
# Files
# -----------------------------------------------

def main():
    try:
        fh = open('../raven.txt', 'r')
        out_file = open('../new.txt', 'w')
        for line in fh.readlines():
            print(line, file = out_file, end='')
    except IOError as e:
        print("Exception ({})".format(e))
    print("Done")
    
if __name__ == "__main__": main()
