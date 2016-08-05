# -----------------------------------------------
# Ruby Examples
#
# Runner for methods.rb
# -----------------------------------------------

require_relative "methods.rb"

# method output
hello

greeting()

greeting("Jenny")

puts "add"
puts "Output: #{add(5, 10)}"
puts

puts "multiply"
puts "Output: #{multiply(8, 8)}"
puts

x = 2
y = 5
result = exponent(2, 5)
puts "exponent"
puts "#{x} to the power of #{y} equals #{result}."
puts

result = add_and_subtract(5, 3) # alternative usage: add, sub = add_and_subtract(5, 3)
puts "add_and_subtract"
puts "add     : #{result[0]}"
puts "subtract: #{result[1]}"
puts

fruits = ['apple', 'cherry', 'pineapple', 'strawberry', 'orange']
longest_word(fruits)
puts

# instance variable will have scope inside the method
@veggies = ['beans', 'spinach', 'green beans', 'carrot', 'onion']
longest_word2
puts
