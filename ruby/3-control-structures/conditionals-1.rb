# -----------------------------------------------
# Ruby Examples
#
# Conditonals - if, elsif, else
# -----------------------------------------------

# if, else, elsif
x = 12

if x > 0 && x <= 5
  puts "x is between 0 and 5"
elsif x > 5 && x <= 10
  puts "x is between 5 and 10"
else
  puts "x is less than 1 or greater than 10"
end
puts ""

name = "John"
puts "This is John" if name == "John"
puts ""