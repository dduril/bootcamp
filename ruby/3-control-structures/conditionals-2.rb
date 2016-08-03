# -----------------------------------------------
# Ruby Examples
#
# Conditonals - unless, case
# -----------------------------------------------

# unless
flag = true
unless flag
  puts "true"
end
puts ""

# case
fruit = "apples"
case
  when fruit == "apples"
    puts "Apples"
  when fruit == "bananas"
    puts "Bananas"
  when fruit == "strawberries"
    puts "Strawberries"
  else
    puts "Kiwis"
end
puts ""

# case - shorter syntax
fruit = "apples"
case fruit
  when "apples"
    puts "Apples"
  when "bananas"
    puts "Bananas"
  when "strawberries"
    puts "Strawberries"
  else
    puts "Kiwis"
end
puts ""

# ternary - boolean ? code1 : code2
puts x == 1 ? "one" : "not one"
puts ""