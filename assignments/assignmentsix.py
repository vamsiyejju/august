#Question - 1
# a lambda function to add two numbers
print(" a lambda function to add two numbers")
a1=int(input('enter a number1 to add: '))
a2=int(input('enter a number2 to add: '))
l=lambda a1,a2 : (a1+a2)
print(l(a1,a2))

print("a lambda function to check whether sum is even or odd")
a1=int(input('enter a number1 to add: '))
a2=int(input('enter a number2 to add: '))
l=lambda a1,a2 : 'even' if (a1+a2)%2==0 else 'odd'
print(l(a1,a2))



print("a lambda function to get product of two numbers")
a1=int(input('enter a number1 to add: '))
a2=int(input('enter a number2 to add: '))
l=lambda a1,a2 : a1*a2
print(l(a1,a2))

#Question - 2 
#filters

print("a programm to filter even or odd")
l=eval(input('enter a numbers  in a single line  seperated by comma: '))
f=filter(lambda n : True if n%2==0 else False,l)
print(list(f))



print("a programm to filter whether number is in between 1 to 100 or not")
l=eval(input('enter a numbers in a single line sperated by comma(,): '))
f=filter(lambda n : True if 1<=n<=100 else False,l)
print(list(f))

print("a programm to filter whether given number is divisible by 3 and 5 ")
l=eval(input('enter the numbers in a single line sperated by comma(,): '))
f=filter(lambda n : True if n%3==0 and n%5==0 else False,l)
print(list(f))


#Question - 3
#Recurrsions
print("print numbers from 1 to given range")
def fun(n,x=1):
    if x>n:
        return
    print(x,end=' ')
    return fun(n,x=x+1)

n=int(input('enter a number upto which you want to print: '))
fun(n)



print(" a programm to check given number is armstrong or not")
def armstrong(n,num,pow,sum=0):
    if n==0:
        return 'armstrong' if num==sum else ('not armstrong')
    return armstrong(n//10,num,pow,sum=sum+((n%10)**pow))

n=int(input('enter a number: '))
print(armstrong(n,n,len(str(n))))



print(" programm to check given number is palindrome or not")
def pal(n,num,rev=0):
    if n==0:
        return 'palindrome' if num==rev else ('not palindrome') 
    return pal(n//10,num,rev=(rev*10)+(n%10))

n=int(input('enter a number that you want to check: '))
print(pal(n,n))