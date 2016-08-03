# -----------------------------------------------
# Ruby Examples
#
# Arrays
# -----------------------------------------------

# arrays
puts "Arrays"
puts "------"
data_set = ["a", "b", "c", 1, 2, ["dog", "cat"], "rabbit"]
puts data_set
data_set << "d"
data_set.push("e")
data_set.push("f")
data_set.pop
puts ""

# print out array properties
puts "data_set  : #{data_set}"
puts "length    : #{data_set.length}"
puts "class     : #{data_set.class}"
puts "object id : #{data_set.object_id}"

# use some of the array methods
puts "inspect   : #{data_set.inspect}"
puts "to_s      : #{data_set.to_s}"
puts "join      : #{data_set.join(", ")}"
puts ""

# another array example
x = "1,2,3,4,5"
puts "x         : #{x}"
puts "class     : #{x.class}" 
y = x.split(",")
puts "y         : #{y}"
puts "class     : #{y.class}"
puts "reverse   : #{y.reverse}"
puts ""

# sort array
x = [21, 55, 10, 3, 48]
puts "x         : #{x}"
puts "sort      : #{x.sort}"
puts ""

# combine arrays
a1 = [0,1,2,3,4]
a2 = [5,6,7,8,9]
a3 = a1 + a2
puts "a1        : #{a1}"
puts "a2        : #{a2}"
puts "a3        : #{a3}"
