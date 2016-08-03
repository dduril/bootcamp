# -----------------------------------------------
# Ruby Examples
#
# Loops - for, loop, while, until
# -----------------------------------------------

# for loop
for i in 0...10 # don't include 10
  puts "i: #{i}" 
end
puts ""

for i in 0..10 # include 10
  puts "i: #{i}" 
end
puts ""

# loop do
x = 0
loop do
  x += 1
  next if x % 3 == 0 # skip numbers evenly divided by three
  puts x
  break if x >= 20
end
puts ""

# while
y = 0
while y <= 10
  puts y
  y += 1
end
puts ""

# until
a = 1

until a >= 5 
  puts a                       
  a += 1                       
end 
puts ""

x = 0
puts x += 2 while x < 100
puts ""

y = 5000
puts y /= 2 until y <= 1
puts ""