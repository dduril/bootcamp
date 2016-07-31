# -----------------------------------------------
# Python Examples
#
# Modules
# -----------------------------------------------

import sys
import os
import urllib.request
import random
import datetime

def main():
    # sys
    print("Python version {}.{}.{}".format(*sys.version_info))
    print(sys.platform)
    print()

    # os
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25))
    print()

    # urllib
    page = urllib.request.urlopen('https://www.python.org/')
    for line in page: print(str(line, encoding='utf_8'), end='')
    print()

    # random
    print(random.randint(1, 1000))
    x = list(range(50))
    print(x)

    # random shuffle
    random.shuffle(x)
    print(x)
    print()

    # datetime
    now = datetime.datetime.now()
    print(now)
    print("{}/{}/{} {}:{}:{}:{}".format(now.month, now.day, now.year, now.hour, now.minute, now.second, now.microsecond))

if __name__ == "__main__": main()
