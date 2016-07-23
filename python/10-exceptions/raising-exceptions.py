# -----------------------------------------------
# Python Examples
#
# Raising Exceptions
# -----------------------------------------------

def main():
    try:
       for line in readFile('../x-raven.tx'): print(line.strip())
    except IOError as e:
        print("Exception: ({})".format(e))
    except ValueError as e:
        print('Error: ', e)

def readFile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('Filename must be a text file')

if __name__ == "__main__": main()
