# -------------------------------------
# Chapter 8 Code Examples
#   Exception Handling
# -------------------------------------

# handle ValueError exception
try:
    number = int(input("Enter an integer: "))
    print("You entered a valid integer: " + str(number) + ".")
except ValueError:
    print("You entered an invalid integer. Please try again.")

# handle all exceptions
try:
    number = int(input("Enter an integer: "))
    print("You entered a valid integer: " + str(number) + ".")
except:
    print("You entered an invalid integer. Please try again.")

# handling multiple exceptions
filename = input("Enter filename: ")
movies = []
try:
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
except FileNotFoundError:
    print("File not found: " + filename)
except OSError:
    print("File found. Error reading file.")
except Exception:
    print("An unexpected error has occurred.")

# handling multiple exceptions using type() and exit()

# import the csv and sys modules
import csv
import sys


filename = input("Enter filename: ")
movies = []
try:
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
except FileNotFoundError as e:
    print("FileNotFoundError:", e)
except OSError as e:
    print("OSError:", e)
except Exception as e:
    print(type(e), e)
    sys.exit()


# try - except - finally example
def read_movies(filename):
    try:
        file = open(filename, newline="")
        try:
            movies = []
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
            return movies
        except Exception as e:
            print(type(e), e)
        finally:
            file.close()
    except FileNotFoundError as e:
        print(e)


# logging an exception
def get_movies(filename):
    try:
        with open(filename, newline="") as file:
            movies = []
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
            return movies
    except Exception as e:
        log_exception(e)
        raise e

        
def log_exception(e):
    # do something here to log exception
    pass
