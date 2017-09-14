# -------------------------------------
# Chapter 6 Code Examples
#   Lists and Tuples
# -------------------------------------

import copy
import random

# lists
scores = [85, 92, 88, 94, 98, 90]
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

# insert() method
fruits.insert(2, "cherries")

# pop() method
i = fruits.index("strawberries")
fruits.pop(i)

# cherries inserted, strawberries removed
for f in fruits:
    print(f)
print()

# len() method
x = len(fruits)
print("Length of fruits[]: ", x, "\n")

# alternative way to print list
print(fruits, "\n")

# process a list
# defined above: scores = [85, 92, 88, 94, 98, 90]
total = 0
for score in scores:
    total += score
print("total: ", total, "\n")

# list of lists
books = [
    ["Thank You for Being Late", 2016, 486],
    ["Only Humans Need Apply", 2016, 276],
    ["Rise of the Robots", 2015, 334]
]

new_book = []
new_book.append("The Inevitable")
new_book.append(2016)
new_book.append(328)
books.append(new_book)

print(books)
print()

for book in books:
    for item in book:
        print(item, end=" | ")
    print()

num_list = [8, 18, 16, 74, 2, 17, 5, 44, 9, 12, 15, 35, 12, 28]
print(num_list, "\n")


# count() method
x = 12
count = num_list.count(x)
print("Count instance of ", x, ": ", count, "\n")

# reverse() method
num_list.reverse()
print("reverse num_list: ", num_list, "\n")

# sort() method
num_list.sort()
print("sort num_list: ", num_list, "\n")

# sorted() method
pizza_toppings = ["mushroom", "onion", "pepperoni", "extra-cheese", "pineapple", "black olives", "sausage", "veggies"]
sorted_pizza_toppings = sorted(pizza_toppings)
print(sorted_pizza_toppings, "\n")

# min(), max() functions
minimum = min(num_list)
maximum = max(num_list)

# choice(), shuffle() functions
choice = random.choice(num_list)
random.shuffle(num_list)

# deepcopy() functions
list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
list_2 = copy.deepcopy(list_1)
list_2[3] = 9
print(list_1, "\n")
print(list_2, "\n")

# tuples
nums = (10.8, 15.2, 18.5, 24.7, 32.9)
ingredients = ("garlic", "olive oil", "salt", "pepper", "tomatoes")
movie = ("Star Wars", "Episode IV: A New Hope", 1977, 123, "PG", "Science Fiction")
