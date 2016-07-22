# -----------------------------------------------
# Python Examples
#
# Regular Expressions - Pre-compiled Regex
# -----------------------------------------------

import re

def main():
    # get the matched lines
    fh = open('../raven.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(line, end='')
    print("\n\n")

if __name__ == "__main__": main()

