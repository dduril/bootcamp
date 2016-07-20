# -----------------------------------------------
# Python Examples
#
# Objects
# -----------------------------------------------

class Employee:
    def __init__(self, status = "New Hire"):
        self.status = status

    def checkStatus(self):
        return self.status

def main():
    e1 = Employee()
    print(type(e1), e1)

    print(e1.checkStatus())

    e2 = Employee("Re-Hire")
    print(e2.checkStatus())

if __name__ == "__main__": main()
