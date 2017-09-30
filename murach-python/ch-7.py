# -------------------------------------
# Chapter 7 Code Examples
#   File I/O
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
movies = ["Casablanca", "It's a Wonderful Life", "Rear Window"]
with open("movies.txt", "w") as file:
    for m in movies:
        file.write(m + "\n")

# read the lines in a file into a list
movies = []
with open("movies.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        movies.append(line)
print(movies)

# write and read a list of numbers
# write the items in a list to a file
years = [2001, 2010, 2061, 3001]
#with open("SpaceOdyssey.txt", "w") as file

# read the items in a list from a file
