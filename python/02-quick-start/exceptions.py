# -----------------------------------------------
# Python Examples
#
# Exceptions
# -----------------------------------------------

try:
    fh = open('xraven.txt')
    for line in fh.readlines():
        print(line)
except IOError as e:
    print("Exception ({})".format(e))

print("Done")