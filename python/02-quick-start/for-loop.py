# -----------------------------------------------
# Python Examples
#
# For Loops
# -----------------------------------------------

fh = open("raven.txt")
for line in fh.readlines():
    print(line, end='')
