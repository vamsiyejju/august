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
