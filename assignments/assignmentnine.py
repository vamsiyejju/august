
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
#calculator task

class calculator():

   def __init__(self,input_01,input_02):
      self.a=input_01
      self.b=input_02

   def add(self):
      return self.a+self.b
   def multiply(self):
      return self.a*self.b
   def divide(self):
      return self.a/self.b
   def subtract(self):
      return self.a-self.b
   
input_1 = int(input("Enter the first number: "))
input_2 = int(input("Enter the second number: "))
print("The entered first and second numbers are : ")
print(input_1, input_2)

my_instance = calculator(input_1,input_2)
choice=1

while choice!=0:
   print("0. Exit")
   print("1. Addition")
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Division")
   choice=int(input("Enter your choice... "))

   if choice==1:
      print("The computed addition result is : ",my_instance.add())
   elif choice==2:
      print("The computed subtraction result is : ",my_instance.subtract())
   elif choice==3:
      print("The computed product result is : ",my_instance.multiply())
   elif choice==4:
      print("The computed division result is : ",round(my_instance.divide(),2))
   elif choice==0:
      print("Exit")
   else:
      print("Sorry, invalid choice!")
print()

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