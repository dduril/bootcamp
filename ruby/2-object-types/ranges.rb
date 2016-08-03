# -----------------------------------------------
# Ruby Examples
#
# Ranges
# -----------------------------------------------

# ranges
puts "Ranges"
puts "------"
x = 1..10   # inclusive - include 10
y = 1...10  # exclusive - exclude 10
a = 'a'..'m'

puts "x              : #{[*x].inspect}" # asterisk(*) splat operator
puts "x.class        : #{x.class}"
puts "x.object_id    : #{x.object_id}"
puts "x.begin        : #{x.begin}"
puts "x.end          : #{x.end}"
puts "x.first        : #{x.first}"
puts "x.last         : #{x.last}"
puts "x.include?(1)  : #{x.include?(1)}"
puts "x.include?(10) : #{x.include?(10)}"
puts ""

puts "y              : #{[*y].inspect}"
puts "y.include?(1)  : #{y.include?(1)}"
puts "y.include?(10) : #{y.include?(10)}"
puts ""

puts "a              : #{[*a].inspect}"
puts "a.include?('a'): #{a.include?('a')}"
puts "a.include?('m'): #{a.include?('n')}"
puts ""
