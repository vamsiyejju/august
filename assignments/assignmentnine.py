
#QUESTION - 1
# Banking operation system


class user():
    username="ntr jr"
    password="ntrjr@9999"
    def create_account(self):
       print("enter the details of account holder")
       self.name=input("enter name  of account holder: ")
       self.age=input("enter age  of account holder : ")
       self.gender=input("enter gender  of account holder : ")
       self.address=input("enter address of account holder : ")
       self.account_number=input("enter account number : ")
       print("Account created successfuly")
class banking(user):
    balence=0
    def deposit(self):
        self.user_name=input("enter user name : ")
        self.passwrd=input("enter password : ")
        if self.name==self.user_name and self.password==self.passwrd:
            print("Logged in successfully")
            self.amount=int(input("enter deposited amount : "))
            self.balence=self.balence+self.amount
            print("The deposited amount is : ",self.balence)
        else:
            print("invalid user name or password")

    def withdraw(self):
        self.user_name=input("enter user name : ")
        self.passwrd=input("enter password : ")
        if self.name==self.user_name and self.password==self.passwrd:
            print("Logged in successfully")
            self.amount=int(input("enter withdrwal amount : "))
            if self.amount>self.balence:
                print("insufficient funds | Available balence is: ",self.balence)
            else:
                self.balence=self.balence-self.amount
                print("account balence after withdrawl :",self.balence)
        else:
            print("invalid user name or password")
    
    def display_balance(self):
        self.user_name=input("enter user name : ")
        self.passwrd=input("enter password : ")
        if self.name==self.user_name and self.password==self.passwrd:
            print("Logged in successfully")
            print("The available balance is : ",self.balence)
        else:
            print("invalid user name or password")

bank=banking()
print("-------select options below-------")
print()
while True:
    user_option=input("enter option : ")
    if user_option=="1":
        bank.create_account()
    elif user_option=="2":
        bank.deposit()
    elif user_option=="3":
        bank.withdraw()
    elif user_option=="4":
        bank.display_balance()
    else:
        print("invalid option")
    next_step=input("enter yes or no for next option : ")
    if next_step=="yes":
        continue
    else:
        break
        
        
#question -2 
#calculator using oops 

# calculator by oops concept 

class calculator:
    def __init__(self):
        self.number1=int(input("enter a number : "))
        self.number2=int(input("enter a number : "))
    def add(self):
        print("The addition of ",self.number1,"and",self.number2,"is : ",self.number1+self.number2)
    def substraction(self):
        print("The substraction of ",self.number1,"and",self.number2,"is : ",self.number1-self.number2)
    def multiplication(self):
        print("The multiplication of ",self.number1,"and",self.number2,"is : ",self.number1*self.number2)
    def division(self):
        print("The division of ",self.number1,"and",self.number2,"is : ",self.number1/self.number2)

while True:

    user=input("enter  function you want : ")
    cal=calculator()
    if user=="add":
        cal.add()
    elif user=="substraction":
        cal.substraction()
    elif user=="multiply":
        cal.multiplication()
    elif user=="division":
        cal.division()
    else:
        print(user,"function not existed in class")
    print()
    next_function=input("enter yes or no for further step : ")
    if next_function=="yes":
        continue
    elif next_function=="no":
        break
    else:
        print("invalid input")
 

#QUESTION - 3
#Reverse the input names in different ways

name=input("enter name : ")
length=len(name)
rev=name[::-1]
splitting=name.split()
output=" ".join(reversed(splitting))
rev1=output[::-1]
print(rev)
print(output)
print(rev1)