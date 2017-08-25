# -------------------------------------
# Chapter 6 Code Examples
#   Lists and Tuples
# -------------------------------------


# lists
scores = [85, 92, 88, 94, 98]
fruits = ["apples", "bananas", "oranges", "pears"]
book = ["Thinking, Fast and Slow", 2011, 499, 16.00]
movies = []

# use of the repetition operator to create a list
temps = [0] * 10
for t in temps:
    print(t)
print()

# get item from list
score = scores[0]
print("score[0]: ", score)
print()

fruit = fruits[2]
print("fruit[2]: ", fruit)
print()

# set item in list
fruits[3] = "strawberries"
for f in fruits:
    print(f)
print()

# append item to list
fruits[3] = "pears"
fruits.append("strawberries")
for f in fruits:
    print(f)
print()

