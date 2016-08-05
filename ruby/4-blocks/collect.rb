# -----------------------------------------------
# Ruby Examples
#
# Blocks - collect
# -----------------------------------------------

array = [1, 2, 3, 4, 5]
print "array: #{array}\n"
print "array cubed: #{array.collect {|i| i ** 3}}"
puts "\n\n"

array = [2, 4, 8, 16]
puts array
puts array.collect {|i| i ** 4}
puts "\n\n"

fruit = ['apple', 'banana', 'cherry', 'orange']
print "#{ fruit.map{ |fruit| fruit.capitalize } }"
