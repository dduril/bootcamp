# -----------------------------------------------
# Ruby Examples
#
# Person class
# -----------------------------------------------

load 'contact_info.rb'

class Person
  include ContactInfo
end

p = Person.new
p.first_name = "John"
p.last_name = "Smith"
p.department = "Technology"
p.job_title = "Front End Developer"
p.city = "Palo Alto"
p.state = "CA"
p.zip_code = "95305"


# Sample Output
# -----------------------------------------------
puts p.full_name
puts p.job_info
puts p.office_info