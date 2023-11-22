# write a python program to reverse a number 

#example 1
num = 12345
c = str(num)[::-1]
print(c)
#example 2
name = "vamsi"
c = (name)[::-1]
print(c)

#armstrong number 
num = input("enter number")
sum = 0
for i in num:
    sum+=int(i)**3
if sum==int(num):
    print('armstrong')
else:
    print("not armstrong")

