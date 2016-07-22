# -----------------------------------------------
# Python Examples
#
# Loop Control
# -----------------------------------------------

def main():
    s = "Hello World!"
    for c in s:
        if c == 'e': break # break at first e, will print 'H'
        print(c)

    print("\n\n")

    s = "Hello World!"
    for c in s:
        if c == 'e': continue # skip the 'e', but continue
        print(c)

if __name__ == "__main__": main()

