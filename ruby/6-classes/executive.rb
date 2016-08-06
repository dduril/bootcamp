# -----------------------------------------------
# Ruby Examples
#
# Executive class
# -----------------------------------------------

class Employee

  # attributes
  attr_accessor :first_name, :last_name, :job_title, :company_name, :pay_group

  # class attribute
  @@company_name = "IT Consulting, Inc."
  @@pay_group = "Salaried"
  @@total_employees = 0

  def self.total_employees
    @@total_employees
  end

  # class method
  def self.all_departments
    ['Accounting', 'Engineering', 'Information Technology', 'Office Services']
  end

  # class method
  # @param [Object] first_name
  # @param [Object] last_name
  # @param [Object] job_title
  def self.create_with_attributes(first_name, last_name, job_title)
    employee = self.new(first_name, last_name, job_title)
    employee.first_name = first_name
    employee.last_name = last_name
    employee.job_title = job_title

    return employee
  end

  # initialize method
  def initialize(first_name, last_name, job_title)
    @first_name = first_name
    @last_name = last_name
    @job_title = job_title
    @@total_employees += 1
    puts "**** New employee.rb added ****"
  end

  # reader and writer methods.rb
  def first_name
    puts @first_name
  end

  def first_name=(value)
    @first_name = value
  end

  def last_name
    puts @last_name
  end

  def last_name=(value)
    @last_name = value
  end

  def job_title
    puts @job_title
  end

  def job_title=(value)
    @job_title = value
  end

  def company_name
    puts @@company_name
  end

  def company_name(value)
    @@company_name = value
  end

  def pay_group
    puts @@pay_group
  end

  def pay_group=(value)
    @@pay_group = value
  end

  # method
  def display_attributes
    puts ""
    puts "Company : " + @@company_name
    puts "Name    : " + @first_name + ' ' + @last_name
    puts "Title   : " + @job_title
  end
end
# end class


class Executive < Employee

end


# Sample Output
# -----------------------------------------------
puts Employee.all_departments.inspect
puts ""

emp1 = Employee.new("John", "Smith", "Full Stack Web Developer")
emp1.display_attributes

emp2 = Employee.create_with_attributes("Lisa", "Jones", "Quality Assurance Engineer")
emp2.display_attributes

exec1 = Executive.new("Bill", "O'Connor", "Chief Technology Officer")
exec1.display_attributes

puts ""
puts "Total Employee Instances : " + Employee.total_employees.to_s