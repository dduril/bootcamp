# -----------------------------------------------
# Ruby Examples
#
# Contact Info module
# -----------------------------------------------

module ContactInfo
  attr_accessor :first_name, :last_name, :department, :job_title, :city, :state, :zip_code

  def full_name
    return "Emp. Name : " + @first_name + " " + @last_name
  end

  def job_info
    return "Department: " + @department + "\nJob Title : " + @job_title
  end
  
  def office_info
    csz = "Location  : " + @city
    csz += ", #{@state}" if @state
    csz += "  #{@zip_code}" if @zip_code
    return csz
  end
  
end