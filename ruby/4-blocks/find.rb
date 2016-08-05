# -----------------------------------------------
# Ruby Examples
#
# Blocks - find
# -----------------------------------------------

# find - find/detect, find_all/select, any?, all?, delete_if
(1..10).find{ |i| print "#{i} " }
print "\n\n"

(1..15).find_all{ |i| puts i if i % 3 == 0 }
print "\n\n"


