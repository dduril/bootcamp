# -----------------------------------------------
# Python Examples
#
# Regular Expressions
# -----------------------------------------------

import re

def main():

    # get the matched lines
    fh = open('../raven.txt')
    for line in fh:
        if re.search('(Len|Neverm)ore', line):
            print(line, end='')
    print("\n\n")

    # get just the matched terms
    fh = open('../raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group())
    print("\n\n")

    # replace the matched terms
    fh = open('../raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore',  line)
        if match:
            print(line.replace(match.group(), '#####'), end='')

if __name__ == "__main__": main()
