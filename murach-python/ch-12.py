# -------------------------------------
# Chapter 12 Code Examples
#   Working with Dictionaries
# -------------------------------------

popular_cities = {"CA": "San Francisco",
          "OR": "Portland",
          "WA": "Seattle",
          "NY": "New York"}
print(popular_cities, "\n")

for code in popular_cities:
    city = popular_cities[code]
    print(city)
print("\n")

# common methods for working with dictionaries
# include get(), pop() and clear()
print(popular_cities.get("OR"))
print(popular_cities.get("UT"))
print(popular_cities.get("UT", "Key not found"), "\n")

city = popular_cities.pop("NY")
print(city, "\n")

for code in popular_cities:
    city = popular_cities[code]
    print(city)
popular_cities.clear()

print("\n")

# looping through keys and values
inventory = {10: "apples", 12: "bananas", 15: "oranges", 8: "pears"}
# keys and values
for i in inventory.keys():
    print(str(i) + "\t" + inventory[i])
print("\n")

# keys and values
for code, name in inventory.items():
    print(str(code) + "\t" + name)
print("\n")

# values
for name in inventory.values():
    print(name)
print("\n")

# convert keys of a dictionary to a list and sort
countries = {"CA": "Canada",
             "US": "United States",
             "MX": "Mexico"}
codes = list(countries.keys())
codes.sort()
for code in codes:
    print(code + " " + countries[code])
print("\n")

# convert two-dimensional list to a dictionary
countries = [["GB", "Great Britain"],
             ["NL", "Netherlands"],
             ["DE", "Germany"]]
countries = dict(countries)
print(countries)
print("\n")

# embedded dictionary examples
mcu = {
    "CA-CW":
        {"title": "Captain America: Civil War",
         "runtime": 147,
         "rating": "PG-13",
         "released": "May 6, 2016"
        },
    "DS":
        {"title": "Doctor Strange",
         "runtime": 115,
         "rating": "PG-13",
         "released": "November 4, 2016"
        },
    "GotG2":
        {"title": "Guardians of the Galaxy Vol. 2",
         "runtime": 136,
         "rating": "PG-13",
         "released": "May 5, 2017"
        }
    }

title = mcu["CA-CW"]["title"]
runtime = mcu["CA-CW"]["runtime"]
rating = mcu["CA-CW"]["rating"]
released = mcu["CA-CW"]["released"]

print(title)
print(str(runtime))
print(rating)
print(released)
