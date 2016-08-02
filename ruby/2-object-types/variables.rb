# -----------------------------------------------
# Ruby Examples
#
# Variables
# -----------------------------------------------


# Declare some variables
x = 100
y = 202.589
z = 12345678912345
s = "Apples and Oranges"


# Output variables and their class types
puts "x:       #{x}"
puts "x.class: #{x.class}\n\n"

puts "y:       #{y}"
puts "y.class: #{y.class}\n\n"

puts "z:       #{z}"
puts "z.class: #{z.class}\n\n"

puts "s:       #{s}"
puts "s.class: #{s.class}\n\n"


# Output string 5 times
5.times { puts "Hello World!" }
puts

5.times do
  puts "Hello World!"
end