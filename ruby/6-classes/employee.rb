# -----------------------------------------------
# Ruby Examples
#
# Employee class
# -----------------------------------------------

class Employee

  # setter or writer method
  def set_name(first_name, last_name)
    @name = first_name + ' ' + last_name
  end

  # getter or reader method
  def get_name
    puts @name
  end

  # Ruby syntactic sugar approach
  def job_title=(job_title)
    @job_title = job_title
  end

  def job_title
    puts @job_title
  end
end

emp1 = Employee.new
emp1.set_name("John", "Smith")
emp1.job_title = "Full Stack Web Developer"
emp1.get_name
emp1.job_title

puts ""
puts "object_id: " + emp1.object_id.to_s
puts "class    : " + emp1.class.to_s
puts

emp2 = Employee.new
emp2.set_name("Lisa", "Jones")
emp2.job_title = "Quality Assurance Engineer"
emp2.get_name
emp2.job_title

puts ""
puts "object_id: " + emp2.object_id.to_s
puts "class    : " + emp2.class.to_s