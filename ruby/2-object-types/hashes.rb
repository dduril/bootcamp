# -----------------------------------------------
# Ruby Examples
#
# Hashes - key-value pairs (dictionary)
# -----------------------------------------------

person = { 
  'emp_no' => 100, 
  'first_name' => 'John', 
  'last_name' => 'Smith', 
  'job_title' => 'Software Engineer', 
  'hire_date' => '07/20/2015'
  }

puts person
puts "person     : #{person}"
puts "class      : #{person.class}"
puts ""

puts "Employee # : #{person['emp_no']}"
puts "First Name : #{person['first_name']}"
puts "Last Name  : #{person['last_name']}"
puts "Job Title  : #{person['job_title']}"
puts "Hire Date  : #{person['hire_date']}"
