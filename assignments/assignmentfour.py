#Question-1
print(" python program to merge two lists")
list1 = eval(input("Enter the first list : "))
list2 = eval(input("Enter the second list : "))
list3 = list1 + list2
print("Merged List:", list3)

#Question-2
print(" python program to find the sum of list elements")
l1=list(eval(input('enter elements : ')))
sum=0
for i in l1:
    sum+=i
print(f'sum of elements in list: {sum}')

#Question-3
print(" python program to print even and odd numbers seperatly in list")
l=list(eval(input('enter elements: ')))
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
print(f'odd numbers: {odd}')
print(f'even numbers: {even}')


#Question-4
print(" python program to delete element of given index in list.")
l=list(eval(input('enter elements: ')))
index=int(input('enter a index position: '))
l.pop(index)
print(f'list after removing element in given index position: {l}')


#Question-5
print("python program to delete given elemet from the list")
l=list(eval(input('enter a group of element: ')))
element=int(input('enter a element to remove from list: '))
l.remove(element)
print(f'list after removing given elements from list: {l}')

#Question-6
print("python program to insert an elemet  at given index location")
l=list(eval(input('enter a group of elements: ')))
index=int(input('enter a index position to insert element at that position'))
element=input('enter a element to insert in a list: ')
l.insert(index,element)
print(f'list after inserting elements at a given index position: {l}')


#Question-7
print("python program to check the sizes of given two lists are same")
v1=list(eval(input('enter a group of elements : ')))
v2=list(eval(input('enter a group of elements : ')))
if (len(v1) == len(v2)):
    print('size of both the lists are same')
else:
    print('size of both the lists are not same')

#Question-8
#8-a
print(" Python function that takes two lists and returns True if they have at least one common member")
list1 = eval(input("Enter the list one : "))
list2 = eval(input("Enter the list two : "))
for x in list1:
    if x in list2:
        print("letter",x,"is commen letter in both lists")

#8-b
print( "Python program to remove a specified column from a given nested list")
l=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
l1=[]
for i in range(int(len(l))):
    element=l[i]
    element.pop(0)
    l1.append(element)
print(f'new list after removing specified elements: {l1}')


       

#Question-9
print("a Python program to convert a list of multiple integers into a single integer")
l=list(eval(input('enter a group of elemets: ')))
l1=''
for i in l:
    l1+=str(i)
print(f'string which formed after adding integers: {l1}')

#Question-10
print("a Python program to remove duplicates from a list")
l1=list(eval(input('enter a group of elements : ')))
l=list(set(l1))
print(f'list after removing duplicates: {l}')

