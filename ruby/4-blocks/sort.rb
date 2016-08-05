# -----------------------------------------------
# Ruby Examples
#
# Blocks - sort
# -----------------------------------------------

array = [2, 7, 1, 9, 5]
puts array.sort{|v1, v2| v1 <=> v2}
puts

fruits = ["apple", "orange", "pineapple", "banana", "cherries", "kiwi"]
puts fruits.sort {|fruit1, fruit2| fruit1.length <=> fruit2.length}
puts

hash = {"c" => 222, "a" => 555, "d" => 111, "b" => 333}
puts "Print hash"
puts hash
puts
puts "To array"
puts hash.to_a
puts
puts "Hash sort on keys"
puts hash.sort {|item1, item2| item1[0] <=> item2[0]}
puts
puts "Hash sort on values"
puts hash.sort {|item1, item2| item1[1] <=> item2[1]}
puts