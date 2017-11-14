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


