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

puts "Output: #{add(5, 10)}"
puts

puts "Output: #{multiply(8, 8)}"
puts

fruits = ['apple', 'cherry', 'pineapple', 'strawberry', 'orange']
longest_word(fruits)
puts

# instance variable will have scope inside the method
@veggies = ['beans', 'spinach', 'green beans', 'carrot', 'onion']
longest_word2
puts
