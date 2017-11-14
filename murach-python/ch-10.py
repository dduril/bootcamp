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
for c in str1:
    print(c)
print("\n")

# slicing a string
str2 = "Hello World, Again"
print(str2)
print("str2[:5]   : ", str2[:5])
print("str2[6:11] : ", str2[6:11])
print("str2[13:]  : ", str2[13:])
print("str2[:]    : ", str2[:])

