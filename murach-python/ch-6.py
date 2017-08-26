# -------------------------------------
# Chapter 6 Code Examples
#   Lists and Tuples
# -------------------------------------


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
