# -----------------------------------------------
# Python Examples
#
# Basic Class Example
# -----------------------------------------------

class Person:
    def announce(self):
        print("Employee Information")

class Employee(Person):
    def __init__(self, empNum, firstName, lastName, jobTitle):
        self.empNum = empNum
        self.firstName = firstName
        self.lastName = lastName
        self.jobTitle = jobTitle

    # setters
    def setEmpNum(self, empNum):
        self.empNum = empNum

    # getters
    def getEmpNum(self):
        return self.empNum

    # add additional getters/setters for other attributes
    # firstName, lastName, jobTitle

    def printEmployee(self):
        super().announce()
        print("Emp#:\t{}".format(self.empNum))
        print("Name:\t{} {}".format(self.firstName, self.lastName))
        print("Title\t{}".format(self.jobTitle))
        print()

def main():
    emp1 = Employee(150, "John", "Smith", "Python Developer")
    print(type(emp1))
    emp1.printEmployee()

    emp1.setEmpNum(175)
    print("Updating Emp#:\t{}\n".format(emp1.getEmpNum()))
    emp1.printEmployee()

    emp2 = Employee(200, "Lisa", "Jones", "Linux System Administrator")
    emp2.printEmployee()

if __name__ == "__main__": main()
