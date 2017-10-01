# -------------------------------------
# Chapter 7 Code Examples
#   File I/O
# -------------------------------------

# Working with text files
# -------------------------------------

# open a text file in write mode and manually close file
outFile = open("test.txt", "w")
outFile.write("Test")
outFile.close()

# with statement to open a text file in write mode and automatically close it
with open("test.txt", "w") as outFile:
    outFile.write("Test")

# with statement to open a text file in read mode and automatically close it
with open("test.txt", "r") as inFile:
    print(inFile.readline())

# write one line to a text file
with open("authors.txt", "w") as file:
    file.write("Thomas Friedman\n")

# append one line to a text file
with open("authors.txt", "a") as file:
    file.write("Daniel Kahneman\n")

# for statement to read text file
with open("authors.txt") as file:
    for line in file:
        print(line, end="")
    print()

# write and read a list of strings
# write the items in a list to a file
FILENAME = "movies.txt"

movies = ["Casablanca", "It's a Wonderful Life", "Rear Window"]
with open(FILENAME, "w") as file:
    for m in movies:
        file.write(m + "\n")

# read the lines in a file into a list
movies = []
with open(FILENAME) as file:
    for line in file:
        line = line.replace("\n", "")
        movies.append(line)
print(movies)

# write and read a list of numbers
# write the items in a list to a file
FILENAME = "arthur-c-clarke.txt"

years = [2001, 2010, 2061, 3001]
with open(FILENAME, "w") as file:
    for year in years:
        file.write(str(year) + "\n")

# read the items in a list from a file
years = []
with open(FILENAME, "w") as file:
    for line in file:
        line = line.replace("\n", "")
        years.append(int(line))
print(years)

# Working with CSV files
# -------------------------------------

movies = [["Star Wars", 1977],
         ["The Empire Strikes Back", 1980],
         ["Return of the Jedi", 1983]]

# import the csv module
import csv

# write to the csv file
with open("star-wars-movies.txt", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(movies)

# read from the csv file
with open("star-wars-movies.txt", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0] + " (" + str(row[1]) + ")")

# Working with binary files
# -------------------------------------

# import the pickle module
import pickle

# write an object to a binary file
with open("movies.bin", "rb") as file:
    pickle.dump(movies, file)

# read an object from a binary file
with open("movies.bin", "rb") as file:
    movie_list = pickle.load(file)
    print(movie_list)
