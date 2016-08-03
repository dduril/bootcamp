# -----------------------------------------------
# Ruby Examples
#
# Iterators
# -----------------------------------------------

# iterators
5.times do
  puts "Hello"
end
puts ""

1.upto(5){ puts "Hello World!" }
puts ""

5.downto(1){ puts "Hello" }
puts ""

(1..5).each{ puts "Hello World!" }
puts ""

1.upto(5) do |i|
  puts i.to_s + ". Hello"
end
puts ""

fruit = ['apple', 'banana', 'cherry', 'lemon', 'lime', 'orange', 'pear', 'strawberry']
print fruit
puts ""
puts ""

fruit.each do |f|
  puts f.capitalize
end
puts ""

for f in fruit
  puts f.capitalize
end
puts ""