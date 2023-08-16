#python program to create table using for and while loop
print("#creating table using for and while loops")
a=int(input("while table:"))
i=1
while(i<11):
    print(a,"x",i,"=",a*i)
    i=i+1
print()

a=int(input("for table:"))
for i in range(1,11):
    print(a,"x",i,"=",a*i)
print()


#python program to create a logic using conditional statements
print("create a program using conditional statement")
list=[1,2,25,99,6,9999]
for num in list:
    if num==2:
        print('num is ',num)
    elif num==25:
        print('found number ', num)
    else:
        print('number not found')

print()


#python program to create a logic using relational operators
print('#CREATE A LOGIC USING LOGICAL AND RELATIONAL OPERATORS')
v=(9,20,13,28,35,54,58,60,)
for num in v:
    if((num==60) or (num==60) ):
        print(num,'scored top in science')
    elif (num>55):
        print(num,'scored second in science')
    elif ((num>=35) and (num<55)):
        print(num,'passed in science')
    else:
        print(num,'failed')