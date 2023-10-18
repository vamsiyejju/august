#QUESTION - 1 :
#Single Inheritance:

class company:
    def companyname(self):
        print("wipro")

class Employee(company):
    def display(self):
        # self.companyname()
        print("vamsi")
        
e = Employee()
e.companyname()
e.display()

#QUESTION - 2 :
# Multiple Inheritance :
class company1:
    def companyname1(self):
        print("wipro")

class company2:
    def companyname2(self):
        print("infosys")

class Employee(company1,company2):
    def method2(self):
        self.companyname1()
        self.companyname2()
        print("vamsi")

e = Employee()
e.method2()

#QUESTION - 3 :
# Multilevel Inheritance:
class grandfather:
    def land(self):
        print("150 acres land")

class father(grandfather):
    def money(self):
        self.land()
        print("100000000 rupees ")

class son(father):
    def car(self):
        self.money()
        print("Range Rover")
s = son()
s.car()

#QUESTION - 4 :
#Hierarchical Inheritance :
class company:
    def companyname(self):
        print("infosys")

class Employee1(company):
    def emp1(self):
        # self.companyname()
        print("vamsi")

class Employee2(company):
    def emp2(self):
        # self.companyname()
        print("sathwika")

e1=Employee1()
e1.companyname()
e1.emp1()
e2=Employee2()
e2.emp2()
