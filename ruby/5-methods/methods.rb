# -----------------------------------------------
# Ruby Examples
#
# Methods
# -----------------------------------------------

# hello
def hello
  puts "Hello World!\n\n"
end

# greeting
def greeting(name = "John")
  puts "Hello #{name}!\n\n"
end

# add
def add(x=nil, y=nil)
  return x + y
end

# longest_word
def longest_word(words=[])
  longest_word = words.inject do |memo, word|
    memo.length > word.length ? memo : word
  end
  puts "Longest word: " + longest_word
end

# longest_word2
def longest_word2
  longest_word = @veggies.inject do |memo, word|
    memo.length > word.length ? memo : word
  end
  puts "Longest word: " + longest_word
end