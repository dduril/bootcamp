# -----------------------------------------------
# Ruby Examples
#
# Booleans
# -----------------------------------------------

# Equal                     ==
# Less then                 <
# Greater than              >
# Less than or equal to     <=
# Greater than or equal to  >=
# Not                       !
# Not equal                 !=
# And                       &&
# Or                        ||

puts "true  : #{true}"
puts "class : #{true.class}"
puts "false : #{false}"
puts "class : #{false.class}"
puts ""

# some exploration with booleans
x = 100
y = 100
puts "#{ x == y }"
y = 90
puts "#{ x > y }"
puts "#{ x < y }"
puts "#{ x >= y }"
puts "#{ x <= y }"

z = 110
puts "#{ x > y && y < z }"
