# -----------------------------------------------
# Python Examples
#
# While Loops
# -----------------------------------------------

def main():
    # simple fibonacci series
    a, b = 0, 1
    while b < 100:
        print(b)
        a, b = b, a + b
    print("Done")

if __name__ == "__main__": main()
