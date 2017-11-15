# -------------------------------------
# Chapter 10 Code Examples
#   Working with Strings
# -------------------------------------

# using an index to access a character of a string
str1 = "Hello World!"
print(str1)
print("str1[0]  : ", str1[0])
print("str1[1]  : ", str1[1])
print("str1[6]  : ", str1[6])
print("str1[11] : ", str1[11], "\n")

# loop over each character in a string
for c in str1:
    print(c)
print("\n")

# print the ordinal value for each character in a string
for c in str1:
    print(ord(c), end=" ")
print("\n")

# slicing a string
str2 = "Hello World, Again"
print(str2)
print("str2[:5]   : ", str2[:5])
print("str2[6:11] : ", str2[6:11])
print("str2[13:]  : ", str2[13:])
print("str2[:]    : ", str2[:])

# len()
print("Length of string: ", str2, " = ", len(str2), "\n")

# check if a string contains all digits
num = "1234"
is_integer = num.isdigit()
print(is_integer)
# can also use: isalpha(str), islower(str), isupper(str)

# check if a string starts with a substring
title = "The Empire Strikes Back"
title_starts_with = title.startswith("The")
print(title_starts_with)
# can also use: endswith(str)

# change a string to title case
movie = "the empire strikes back"
movie = movie.title()
print(movie, "\n")
# can also use: lower(), upper()

# remove whitespace from start and end of a string
phone_num = "   408 445-1250    "
print(phone_num)
phone_num = phone_num.strip()
print(phone_num, "\n")

# removing and replacing dashes with replace()
prod_num = "1234-567890-4321-50"
print(prod_num)
prod_num = prod_num.replace("-", "")
print(prod_num, "\n")

prod_num = "1234-567890-4321-50"
print(prod_num)
prod_num = prod_num.replace("-", " ")
print(prod_num, "\n")

# splitting a string on whitespace
quotation = "To be or not to be? that is the question."
print(quotation)
words = quotation.split()
print(words[0])
print(words[3])
print(words[7])
print(words[-1])
print(words[9], "\n")

# splitting a date on a delimiter
date = "11/15/2017"
date = date.split("/")
month = int(date[0])
day = int(date[1])
year = int(date[2])
print(str(month))
print(str(day))
print(str(year), "\n")

# splitting a address on a delimiter
address = "John Smith|1500 Coffee Lane|Portland|OR|97035"
address = address.split("|")
print(address[0])
print(address[1])
print(address[2] + ", " + address[3] + " " + address[4] + "\n")

# joining strings
first_name = ""
last_name = ""
full_name = first_name + ", " + last_name + "\n"

# joining items in a list
scifi_movies = ["Alien", "Avatar", "Bladerunner", "Chappie", "Robocop"]
scifi_movies = " | ".join(scifi_movies)
print(scifi_movies, "\n")

# joining characters
letters = "DEVOPS"
letters = " ".join(letters)
print(letters, "\n")

