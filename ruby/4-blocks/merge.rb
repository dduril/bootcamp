# -----------------------------------------------
# Ruby Examples
#
# Blocks - merge
# -----------------------------------------------

hash1 = {"a" => 100, "b" => 200, "c" => 300}
hash2 = {"d" => 400, "e" => 500}
puts hash1.merge(hash2)
puts "\n\n"

hash1 = {"a" => 100, "b" => 200, "c" => 300}
hash2 = {"b" => 400, "e" => 500}
puts hash1.merge(hash2)
puts "\n\n"

