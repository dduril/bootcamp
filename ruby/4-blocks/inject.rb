# -----------------------------------------------
# Ruby Examples
#
# Blocks - inject
# -----------------------------------------------

numbers = [*1..10]
print "numbers: #{numbers.inspect}\n"
sum = numbers.inject {|memo, n| memo + n}
print "sum: #{sum}"
print "\n"

product = numbers.inject {|memo, n| memo * n}
print "product: #{product}"
print "\n\n"

fruits = ['apple', 'pear', 'banana', 'strawberry', 'pineapple']
print "fruits #{fruits.inspect}\n"
longest_word = fruits.inject do |memo, fruit|
  if memo.length > fruit.length
    memo
  else
    fruit
  end
end
puts "longest_word: #{longest_word}"
puts

side_nav = ['Home', 'Products', 'Solutions', 'Downloads', 'About Us']
print "side_nav #{side_nav.inspect}\n"
menu_length = side_nav.inject(10) {|memo, item| memo + item.length}
puts "menu_length: #{menu_length}"